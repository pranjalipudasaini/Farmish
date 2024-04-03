from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['farmer_name',
    'product_name',
    'rate',
    'quantity', 
    'categories',
    'product_image'
    ]


