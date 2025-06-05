"""
Shopping List Models Module

Slouží k definici datových struktur aplikace, které se automaticky převádějí na databázové tabulky.
"""

from django.db import models
from django.contrib.auth.models import User

class ItemsList(models.Model):
	"""
	Reprezentuje položku v nákupním seznamu s doplňujícími informacemi.
	Každá položka patří konkrétnímu uživateli, může být zařazena do kategorie, 
 	označena jako dokončená a volitelně může obsahovat obrázek a popis.
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
		"""
  		Vrací textovou reprezentaci položky nákupu.
  		"""
		return self.itemname

	class Meta:
		"""
  		Možnosti třídy Meta pro model ItemsList.
  		"""
		ordering = ['-date_added']  # Řadí položky podle data přidání, nejnovější jako první.

