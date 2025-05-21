"""
Shopping List URLs Configuration

This module defines the URL routing for the shopping list application.
It includes routes for CRUD operations on shopping items, user authentication,
and various utility endpoints.

All routes requiring authentication are protected by the @login_required decorator
in their respective view functions.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Main application URLs
    path("", views.index, name="index"),  # Main shopping list view
    path("add/", views.addItem, name="add"),  # Add new item
    path("complete/<int:item_id>/", views.completeItem, name="complete"),  # Mark item as complete
    path("deleteitem/<int:item_id>/", views.deleteItem, name="deleteitem"),  # Delete specific item
    path("deleteall/", views.deleteAll, name="deleteall"),  # Delete all items
    path("item/<int:item_id>/", views.item_detail, name="item_detail"),  # View item details
    path("item/<int:item_id>/edit/", views.edit_item, name="edit_item"),  # Edit item
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),  # User login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # User logout
    path('register/', views.register, name='register'),  # User registration
]
