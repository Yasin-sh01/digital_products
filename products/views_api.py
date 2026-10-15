from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True, context = {'request' : request})
        return Response(serializer.data)
    
class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context = {'request' : request})
        return Response(serializer.data)
    

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)

class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk = pk)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class FileListView(APIView):
    def get(self, request, pk):
        files = File.objects.filter(product_id=pk)
        if not files.exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(files, many = True, context = {'request' : request})
        return Response(serializer.data)

class FileDetailView(APIView):
    def get(self, request, pk):
        try:
            file = File.objects.get(pk = pk)
        except File.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file, context = {'request' : request})
        return Response(serializer.data)
