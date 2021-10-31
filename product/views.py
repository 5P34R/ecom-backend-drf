from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Catagory
from .serializers import ProductSerializer

class ProductListView(APIView):
    def get(self, request):
        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)

class ProductDeatiledView(APIView):
    def get(self, request, pk):
        prod = Product.objects.get(pk=pk)
        serializer = ProductSerializer(prod, many=False)
        return Response(serializer.data)