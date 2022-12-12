from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.


# CRUD OPERATIONS

class ProductViewSet(viewsets.ViewSet):
    def list(self,request): # /api/products
        pass

    
    def create(self,request):   # /api/products
        pass

    def retrive(self,request,pk=None):   # /api/products/<str:id>
        pass  

    def update(self,request,pk=None):
        pass

    def destroy(self,request,pk=None):
        pass



    

