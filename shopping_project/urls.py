"""
Main URL Configuration for Shopping List Project

This module defines the root URL configuration for the entire project.
It includes:
- Admin interface URLs
- Shopping list application URLs
- Media file serving for development

The URL patterns are structured to provide a clean and intuitive URL scheme,
with the shopping list application handling the root URL ('/').
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Main URL patterns
urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    
    # Shopping list application - handles all main URLs
    path("", include("shopping_list.urls"))
]

# Add media file serving for development
# In production, these should be served by the web server
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
