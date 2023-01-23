from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
path("products/", views.products, name= "product"),
path("product/<pk>/", views.product, name= "product"),


]