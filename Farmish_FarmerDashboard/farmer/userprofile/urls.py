from django.urls import path
from .views import add_product, my_shop

urlpatterns = [
    path('Myshop/', my_shop, name='my_shop'),
    path('add_product/', add_product, name='add_product'),  # Changed URL pattern
]
