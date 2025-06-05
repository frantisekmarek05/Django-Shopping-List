"""
WSGI Configuration for Shopping List Project

Tento modul obsahuje konfiguraci WSGI aplikace, kterou využívá vývojový server Djanga
a také produkční servery jako Gunicorn nebo uWSGI.
Zpřístupňuje tzv. WSGI objekt jako proměnnou na úrovni modulu s názvem application.

Konfigurace WSGI slouží k nasazení aplikace v produkčním prostředí.
Zajišťuje rozhraní mezi webovým serverem a Django aplikací.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_project.settings')

# Initialize WSGI application
application = get_wsgi_application()
