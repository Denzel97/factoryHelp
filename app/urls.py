from django.urls import path
from .views import CompanyListCreateView, ProductListCreateView, CategoryListCreateView

urlpatterns = [
    path('api/companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]