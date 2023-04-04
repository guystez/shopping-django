from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 


app_name = 'product'

urlpatterns = [
path("products/", views.products, name= "product"),
path("cart/", views.cart_list, name= "cart_list"),
path("checkout/", views.checkout, name= "checkout"),
path("product/<pk>/", views.product, name= "product"),
path("deletecart/<pk>/", views.deletetfromcart, name= "deletefromcart"),
path("updatecart/<pk>/", views.updatecart, name= "updatecart"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)