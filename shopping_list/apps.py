"""
Shopping List Application Configuration

Definuje konfigurační třídu aplikace, která říká Djangu název aplikace a může obsahovat další specifická nastavení nebo chování při jejím spuštění.
"""

from django.apps import AppConfig


class ShoppingListConfig(AppConfig):
    """
    Konfigurační třída pro aplikaci nákupního seznamu.
    Tato třída se stará o základní nastavení aplikace, například o její název, 
    a může být rozšířena o zpracování signálů nebo další specifická nastavení dané aplikace.
    """
    name = 'shopping_list'
    verbose_name = 'Shopping List Manager'
