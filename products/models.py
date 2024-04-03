# products/models.py
from django.db import models

class Product(models.Model):
    farmer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    categories = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product_name
