from django.db import models
from django.db.models.fields import CharField

class LowercaseCharField(CharField):
	def get_db_prep_value(self, value, connection, prepared=False):
		return value.lower()

class ItemCategory(models.Model):
	name = LowercaseCharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "item category"
		verbose_name_plural = "item categories"
		ordering = ['name']
			

class Item(models.Model):
	name = LowercaseCharField(max_length=50, unique=True)
	category = models.ForeignKey(ItemCategory, null=True, blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


