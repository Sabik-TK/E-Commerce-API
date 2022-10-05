from django.db import models
from apps.category.models import Category
# Create your models here.

class Product(models.Model):
    name            = models.CharField(max_length=200, unique=True)
    description     = models.TextField(max_length=2500, blank=True)
    price           = models.IntegerField()
    mrp             = models.IntegerField(default= price,null=True)
    thumbnail       = models.ImageField(upload_to='product/thumbnail')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sold_quantity   = models.IntegerField(default=0)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)


    def offer(self):
        product_offer = int(((self.mrp - self.price)/self.mrp) * 100)
        return product_offer
 
    def __str__(self): 
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='product/extra_images')


   

