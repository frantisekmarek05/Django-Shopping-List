"""
Shopping List Models Module

This module defines the data models for the shopping list application.
It contains the ItemsList model which represents a shopping list item
with various attributes such as name, category, completion status, and optional image.
"""

from django.db import models
from django.contrib.auth.models import User

class ItemsList(models.Model):
	"""
	Represents a shopping list item with associated metadata.
	
	Each item belongs to a specific user and can be categorized, marked as completed,
	and optionally include an image and description.
	"""

	CATEGORY_CHOICES = [
		('dairy', 'Mléčné výrobky'),
		('vegetables', 'Ovoce a zelenina'),
		('frozen', 'Mražené potraviny'),
		('meal', 'Hotová jídla'),
		('bread', 'Pečivo'),
		('other', 'Ostatní')
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='User who owns this item')
	itemname = models.CharField(max_length=200, help_text='Name of the shopping item')
	description = models.TextField(blank=True, null=True, help_text='Optional description of the item')
	image = models.ImageField(upload_to='items_images/', blank=True, null=True, help_text='Optional image of the item')
	completed = models.BooleanField(default=False, help_text='Whether the item has been purchased')
	date_added = models.DateTimeField(auto_now_add=True, help_text='Date and time when the item was added')
	category = models.CharField(
		max_length=20,
		choices=CATEGORY_CHOICES,
		default='other',
		help_text='Category of the shopping item'
	)

	def __str__(self):
		"""Returns a string representation of the shopping item."""
		return self.itemname

	class Meta:
		"""Meta options for the ItemsList model."""
		ordering = ['-date_added']  # Orders items by date added, newest first

