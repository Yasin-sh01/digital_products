from rest_framework import serializers
from .models import Category, File, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'id')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('title', 'file', 'File_type', 'id')

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')
    categories = CategorySerializer(many = True)
    file = FileSerializer(many = True)
    class Meta:
        model = Product
        fields = ('url', 'title', 'description', 'avatar', 'categories', 'file', 'id')
