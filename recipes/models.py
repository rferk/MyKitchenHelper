from django.db import models
from django.db.models.fields import CharField

class LowercaseCharField(CharField):
	def get_db_prep_value(self, value, connection, prepared=False):
		return value.lower()

class Recipe(models.Model):
	name = LowercaseCharField(max_length=50, unique=True)

	def first_letter(self):
		return self.name and self.name[0] or ''

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

