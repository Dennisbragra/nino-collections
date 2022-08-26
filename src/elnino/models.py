from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Product(models.Model):
	productType = models.CharField(max_length=150)

	def __str__(self):
		return self.productType


class ProductDetails(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	name = models.CharField(max_length=150)
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits= 19, decimal_places = 2)
	quantity = models.IntegerField()
