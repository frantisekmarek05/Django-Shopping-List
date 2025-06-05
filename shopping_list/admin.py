"Slouží k registraci modelů do Django administrace, kde je pak lze snadno spravovat přes webové rozhraní."

from django.contrib import admin

from .models import ItemsList

admin.site.register(ItemsList)
