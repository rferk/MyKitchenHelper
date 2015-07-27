from django.db import models
from items.models import Item

class Inventory(models.Model):
	item = models.OneToOneField(Item, null=True, blank=True)
	stock = models.PositiveSmallIntegerField(default="1")
	tracked = models.BooleanField(default=0)
	threshold = models.PositiveSmallIntegerField(default="0")

	def name(self):
		return self.item.name

	def first_letter(self):
		return self.item.name and self.item.name[0] or ''

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
		verbose_name = "inventory item"
		verbose_name_plural = "inventory items"
		ordering = ['item']

	def __str__(self):
		if self.item:
			return self.item.name
		else:
			return "inventory item"