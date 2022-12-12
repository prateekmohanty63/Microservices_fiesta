from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.


# CRUD OPERATIONS

class ProductViewSet(viewsets.ViewSet):
    def list(self,request): # /api/products
        products=Product.objects.all()

        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

    
    def create(self,request):   # /api/products
        pass

    def retrive(self,request,pk=None):   # /api/products/<str:id>
        pass  

    def update(self,request,pk=None):
        pass

    def destroy(self,request,pk=None):
        pass



    

