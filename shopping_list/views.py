"""
Shopping List Views Module

This module contains all the view functions for the shopping list application.
It handles user authentication, CRUD operations for shopping list items,
and various utility functions for managing the shopping list.

The views support both regular HTTP requests and AJAX calls, providing
appropriate responses based on the request type.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import *
import json
import logging

logger = logging.getLogger(__name__)

def register(request):
	"""
	Handle user registration.
	
	Processes both GET (registration form) and POST (form submission) requests.
	On successful registration, logs in the user and redirects to the index page.
	"""
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Registration successful!')
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'registration/register.html', {'form': form})

@login_required
def index(request):
	"""
	Display the main shopping list page.
	
	Shows all shopping items grouped by their categories.
	Only displays non-empty categories and includes category translations.
	Requires user authentication.
	"""
	# Get all items and group them by category
	all_items = ItemsList.objects.filter(user=request.user)
	items_by_category = {
		'dairy': all_items.filter(category='dairy'),
		'vegetables': all_items.filter(category='vegetables'),
		'frozen': all_items.filter(category='frozen'),
		'meal': all_items.filter(category='meal'),
		'bread': all_items.filter(category='bread'),
		'other': all_items.filter(category='other')
	}
	
	# Remove empty categories
	items_by_category = {k: v for k, v in items_by_category.items() if v.exists()}
	
	category_names = {
		'dairy': 'Mléčné výrobky',
		'vegetables': 'Ovoce a zelenina',
		'frozen': 'Mražené potraviny',
		'meal': 'Hotová jídla',
		'bread': 'Pečivo',
		'other': 'Ostatní'
	}
	
	return render(request, "shopping_list/index.html", {
		"items_by_category": items_by_category,
		"category_names": category_names,
		"items_saved": all_items.exists()
	})

@login_required
def addItem(request):
	"""
	Add a new shopping list item.
	
	Handles POST requests for creating new items.
	Supports both regular form submissions and AJAX requests.
	Can handle image uploads and validates required fields.
	"""
	if request.method == 'POST':
		item_name = request.POST.get('item', '').strip()
		category = request.POST.get('category', 'other')
		
		if not item_name:
			if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
				return JsonResponse({
					'success': False,
					'error': 'Item name is required'
				}, status=400)
			messages.error(request, 'Item name is required')
			return redirect('index')

		try:
			# Create new item
			new_item = ItemsList(
				itemname=item_name,
				user=request.user,
				category=category
			)
			
			# Handle image if provided
			if 'image' in request.FILES:
				try:
					new_item.image = request.FILES['image']
					logger.error(f"Image upload attempted: {request.FILES['image'].name}")
				except Exception as img_error:
					logger.error(f"Image upload error: {str(img_error)}")
					messages.error(request, f'Image upload failed: {str(img_error)}')
					return redirect('index')
			
			# Save the item
			try:
				new_item.save()
				logger.info(f"Item saved successfully: {new_item.id}")
			except Exception as save_error:
				logger.error(f"Item save error: {str(save_error)}")
				messages.error(request, f'Failed to save item: {str(save_error)}')
				return redirect('index')
			
			if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
				return JsonResponse({
					'success': True,
					'item': {
						'id': new_item.id,
						'itemname': new_item.itemname,
						'category': new_item.category,
						'image_url': new_item.image.url if new_item.image else None,
						'date_added': new_item.date_added.strftime('%B %d, %Y, %I:%M %p'),
						'completed': new_item.completed
					}
				})
			
			messages.success(request, 'Item added successfully!')
			return redirect('index')
			
		except Exception as e:
			logger.error(f"Error adding item: {str(e)}")
			if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
				return JsonResponse({
					'success': False,
					'error': f'Failed to add item: {str(e)}'
				}, status=500)
			messages.error(request, f'Failed to add item: {str(e)}')
			return redirect('index')
			
	return redirect('index')

@login_required
def item_detail(request, item_id):
	"""
	Display detailed information about a specific shopping list item.
	
	Shows all item attributes and allows for viewing the full image if present.
	"""
	item = get_object_or_404(ItemsList, id=item_id, user=request.user)
	return render(request, 'shopping_list/item_detail.html', {'item': item})

@login_required
def edit_item(request, item_id):
	"""
	Handle item editing functionality.
	
	Supports both GET (form display) and POST (update) requests.
	Handles image uploads and deletions.
	Validates input data and provides appropriate error messages.
	"""
	try:
		item = get_object_or_404(ItemsList, id=item_id, user=request.user)
	except:
		if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			return JsonResponse({
				'success': False,
				'error': 'Item not found'
			}, status=404)
		messages.error(request, 'Item not found')
		return redirect('index')

	if request.method == 'POST':
		try:
			# Get and validate form data
			itemname = request.POST.get('itemname', '').strip()
			category = request.POST.get('category', 'other')
			completed = request.POST.get('completed') == 'true'

			if not itemname:
				return JsonResponse({
					'success': False,
					'error': 'Item name is required'
				}, status=400)

			# Update fields
			item.itemname = itemname
			item.category = category
			item.completed = completed

			# Handle image
			if 'image' in request.FILES:
				try:
					# Delete old image if exists
					if item.image:
						item.image.delete(save=False)
					item.image = request.FILES['image']
				except Exception as e:
					logger.error(f"Image upload error: {str(e)}")
					return JsonResponse({
						'success': False,
						'error': 'Failed to upload image'
					}, status=400)

			# Save the item
			item.save()

			# Prepare response data
			response_data = {
				'success': True,
				'item': {
					'id': item.id,
					'itemname': item.itemname,
					'category': item.category,
					'image_url': item.image.url if item.image else None,
					'date_added': item.date_added.strftime('%B %d, %Y, %I:%M %p'),
					'completed': item.completed
				}
			}

			return JsonResponse(response_data)

		except Exception as e:
			logger.error(f"Error updating item: {str(e)}")
			return JsonResponse({
				'success': False,
				'error': 'An error occurred while updating the item'
			}, status=500)

	# GET request
	if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
		return JsonResponse({
			'success': True,
			'item': {
				'id': item.id,
				'itemname': item.itemname,
				'category': item.category,
				'image_url': item.image.url if item.image else None,
				'date_added': item.date_added.strftime('%B %d, %Y, %I:%M %p'),
				'completed': item.completed
			}
		})

	return render(request, 'shopping_list/edit_item.html', {'item': item})

@login_required
def completeItem(request, item_id):
	"""
	Mark a shopping list item as completed.
	
	Updates the completed status of an item and redirects back to the index page.
	Only allows users to complete their own items.
	"""
	try:
		item = ItemsList.objects.get(id=item_id)
		if item.user == request.user:
			item.completed = True
			item.save()
			messages.success(request, 'Item marked as completed!')
	except ItemsList.DoesNotExist:
		messages.error(request, 'Item not found!')
	return redirect('index')

@login_required
def deleteItem(request, item_id):
	"""
	Delete a specific shopping list item.
	
	Removes both the item record and any associated image file.
	Only allows users to delete their own items.
	"""
	try:
		item = ItemsList.objects.get(id=item_id)
		if item.user == request.user:
			if item.image:
				item.image.delete()
			item.delete()
			messages.success(request, 'Item deleted successfully!')
	except ItemsList.DoesNotExist:
		messages.error(request, 'Item not found!')
	return redirect('index')

@login_required
def deleteAll(request):
	"""
	Delete all shopping list items for the current user.
	
	Removes all items and their associated image files.
	Provides feedback through a success message.
	"""
	items = ItemsList.objects.filter(user=request.user)
	for item in items:
		if item.image:
			item.image.delete()
	items.delete()
	messages.success(request, 'All items deleted successfully!')
	return redirect('index')