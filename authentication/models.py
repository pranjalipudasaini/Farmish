from django.db import models

#Banner 
class Banner(models.Model):
    img = models.CharField(max_length = 200)
    alt_tect = models.CharField(max_length = 300)

class Category(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "cat_imgs/", null = True)

    def __str__(self):
        return self.title

#Farmer
class Farmer(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to ="farmer_imgs/", null = True )

    def __str__(self):
        return self.title
    
#Type
class Type(models.Model):
    title = models.CharField(max_length = 100)
    color_code = models.CharField(max_length= 100)
    def __str__(self):
        return self.title

#Size
class Size(models.Model):
    title = models.CharField(max_length = 100)
   
        
#Product model
class Product(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = "products_imgs/")
    slug = models.CharField(max_length = 400)
    detail = models.TextField()
    specs = models.TextField()
    
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete = models.CASCADE)
    size = models.ForeignKey(Size, on_delete = models.CASCADE)
    type = models.ForeignKey(Type, on_delete = models.CASCADE)
    status = models.BooleanField(default = True)
    

    def __str__(self):
        return self.title

#product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    type = models.ForeignKey(Type, on_delete = models.CASCADE)
    size = models.ForeignKey(Size, on_delete = models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product.title
