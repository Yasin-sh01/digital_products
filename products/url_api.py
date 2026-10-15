from django.urls import path
from .views_api import (ProductListView, ProductDetailView, CategoryListView, FileListView,
CategoryDetailView, FileDetailView)

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('files/product/<int:pk>/', FileListView.as_view()),
    path('file/<int:pk>/', FileDetailView.as_view()),
]