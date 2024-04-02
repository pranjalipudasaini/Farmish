from django.urls import path
from .views import product_detail, search

urlpatterns = [
    path('search/', search, name='search'),
    path('<slug:slug>/', product_detail, name='product_detail'),    
    
]

