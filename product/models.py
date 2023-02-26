from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    created = models.DateField(auto_now_add=True)
    updated =  models.DateField(auto_now=True)
    archive = models.BooleanField(default=False)
    image = models.ImageField(null=True , blank=True, default='/placeholder.png')
    

class Cart_new(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,unique=True)
    quantity=models.SmallIntegerField()

class Orders(models.Model):
    product = models.ManyToManyField(Product)
    quantity=models.SmallIntegerField(null=True)
    date =models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.SmallIntegerField()
    date =models.DateTimeField(auto_now=True)
