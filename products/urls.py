# products/urls.py
from django.urls import path
from .views import add_product, product_list

urlpatterns = [
    path('', add_product, name='add_product'),
    path('shop/', product_list, name='product_list'),
]
