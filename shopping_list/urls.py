"""
Shopping List URLs Configuration

slouží k propojení URL adresy s konkrétními view funkcemi (tedy co se má zobrazit, když uživatel navštíví určitou adresu).
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Hlavní URL adresy aplikace
    path("", views.index, name="index"),  # Hlavní zobrazení nákupního seznamu
    path("add/", views.addItem, name="add"),  # Přidání nové položky
    path("complete/<int:item_id>/", views.completeItem, name="complete"),  # Označení položky jako dokončené
    path("deleteitem/<int:item_id>/", views.deleteItem, name="deleteitem"),  # Smazání konkrétní položky
    path("deleteall/", views.deleteAll, name="deleteall"),  # Smazání všech položek
    path("item/<int:item_id>/", views.item_detail, name="item_detail"),  # Zobrazení detailu položky
    path("item/<int:item_id>/edit/", views.edit_item, name="edit_item"),  # Úprava položky

    # URL adresy pro přihlášení a registraci
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Přihlášení uživatele
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Odhlášení uživatele
    path('register/', views.register, name='register'),  # Registrace uživatele

]
