from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers

# To View All Product in the API 
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def delete(request, self, *args, **kwargs):
        Product.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# To Retrieve, Update, Delete Product in the API 
class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'