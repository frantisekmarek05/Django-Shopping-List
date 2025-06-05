"""
Main URL Configuration for Shopping List Project

Tento modul definuje hlavní (kořenovou) URL konfiguraci pro celý projekt.
Obsahuje:
    URL adresy pro administrátorské rozhraní
    URL adresy pro aplikaci nákupního seznamu
    Obsluhu mediálních souborů během vývoje
Struktura URL adres je navržena tak, aby byla přehledná a logická –
hlavní URL adresa ('/') je předána aplikaci nákupního seznamu, která ji obsluhuje.
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
