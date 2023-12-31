from django.shortcuts import render
from rest_framework import generics
from .models import Company, Product, Category
from .serializers import CompanySerializer, ProductSerializer, CategorySerializer


# Create your views here.
class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
