
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from django.contrib import messages

# Create your views here.




@api_view(['GET', 'POST','ADD'])
def cart(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET': #list products
        cart = Cart.objects.filter(in_cart = "True")
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': #create new product
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete products
@api_view(['DELETE', 'PUT','GET','ADD'])
def product(request,pk):
    if request.method == 'GET': #list products
        products = Cart.objects.get(id=pk)
        serializer = CartSerializer(products)
        return Response(serializer.data) 

    if request.method == 'DELETE':
        prod = Cart.objects.get(id=pk)
        prod.archive=True
        prod.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        prod = Cart.objects.get(pk=pk)
        serializer = CartSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
