"""
WSGI Configuration for Shopping List Project

This module contains the WSGI application configuration used by Django's development server
and other production servers such as Gunicorn or uWSGI. It exposes the WSGI callable
as a module-level variable named 'application'.

The WSGI configuration is used to serve the application in a production environment.
It provides the interface between the web server and the Django application.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_project.settings')

# Initialize WSGI application
application = get_wsgi_application()
