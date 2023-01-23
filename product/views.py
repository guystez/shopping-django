from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.contrib import messages
# from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def products(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET': #list products
        products = Product.objects.filter(archive = "False")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': #create new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete products
@api_view(['DELETE', 'PUT','GET'])
def product(request,pk):
    if request.method == 'GET': #list products
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data) 

    if request.method == 'DELETE':
        prod = Product.objects.get(id=pk)
        prod.archive=True
        prod.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        prod = Product.objects.get(pk=pk)
        serializer = ProductSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

