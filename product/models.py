from django.db import models
from django.utils import timezone
import datetime

def default_category_id():
    # Create categories if they don't exist
    if not Category.objects.filter(name='Fresh Produce').exists():
        Category.objects.create(name='Fresh Produce')

    if not Category.objects.filter(name='Pantry Staples').exists():
        Category.objects.create(name='Pantry Staples')

    if not Category.objects.filter(name='Dairy & Eggs').exists():
        Category.objects.create(name='Dairy & Eggs')

    if not Category.objects.filter(name='Meat').exists():
        Category.objects.create(name='Meat')

    # Retrieve the categories
    fresh_category = Category.objects.get(name='Fresh Produce')
    pantry_category = Category.objects.get(name='Pantry Staples')
    dairy_category = Category.objects.get(name='Dairy & Eggs')
    meat_category = Category.objects.get(name='Meat')

    return fresh_category, pantry_category, dairy_category, meat_category

#Categories of Products
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	#@daverobb2011
	class Meta:
		verbose_name_plural = 'categories'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Rate (NPR)')
    total_quantity = models.PositiveIntegerField(default=0)
    available_quantity = models.PositiveIntegerField(default=0)
    sold_quantity = models.PositiveIntegerField(default=0)
    product_image = models.ImageField(upload_to='product_images/', max_length=None)
    Listed_Date = models.DateTimeField(default=timezone.now)
    lifespan = models.IntegerField(default=0, help_text="Lifespan in days")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=default_category_id)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the product first

    def __str__(self):
        return self.product_name

    class Meta:
        app_label = 'product'
    
# Customers
class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
 

      

