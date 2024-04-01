from django.contrib import admin
from .models import Category, Farmer, Type, Size, Product, ProductAttribute
# Register your models here.

admin.site.register(Category)
admin.site.register(Farmer)
admin.site.register(Type)
admin.site.register(Size)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'farmer', 'type','size', 'status')
    list_editable =('status', ) 
admin.site.register(Product, ProductAdmin)     

#Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
admin.site.register(ProductAttribute, ProductAttributeAdmin)  
