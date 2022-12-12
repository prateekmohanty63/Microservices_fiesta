from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# CRUD OPERATIONS

class ProductViewSet(viewsets.ViewSet):
    def list(self,request): # /api/products
        products=Product.objects.all()

        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

    
    def create(self,request):   # /api/products
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retrive(self,request,pk=None):   # /api/products/<str:id>
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer (product)

        return Response(serializer.data)

    def update(self,request,pk=None):
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)


    def destroy(self,request,pk=None):
        product=Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    

