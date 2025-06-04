"""
Shopping List Application Configuration

This module contains the Django application configuration for the shopping list app.
It defines the app name and any application-specific settings or signals.
"""

from django.apps import AppConfig


class ShoppingListConfig(AppConfig):
    """
    Configuration class for the Shopping List application.
    
    This class handles the application's configuration, including app name,
    and can be extended to include signal handlers and app-specific settings.
    """
    name = 'shopping_list'
    verbose_name = 'Shopping List Manager'
