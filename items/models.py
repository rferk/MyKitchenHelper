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
	category = models.ForeignKey(ItemCategory)
	stock = models.PositiveSmallIntegerField(default="1")
	tracked = models.BooleanField(default=0)
	threshold = models.PositiveSmallIntegerField(default="0")

	def first_letter(self):
		return self.name and self.name[0] or ''

	def status(self):
		if not self.tracked:
			return {"status":"na", 	"order":3}
		elif self.stock == 0:
			return {"status":"out", "order":0}
		elif self.stock >= self.threshold:
			return {"status":"ok", 	"order":2}
		else:
			return {"status":"low", "order":1}

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


