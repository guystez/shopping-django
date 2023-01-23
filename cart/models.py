from django.db import models

from product.models import Product

# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(null=False,default=0)
    in_cart = models.BooleanField(default=False)
    