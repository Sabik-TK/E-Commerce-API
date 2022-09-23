from django.db import models
# Create your models here.

class Category(models.Model):
    name           = models.CharField(max_length= 50, unique=True)
    thumbnail               = models.ImageField(upload_to='photos/categories', blank = True)
    category_no             = models.IntegerField(unique=True)

    class Meta:
        ordering            = ['category_no']
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):

    name                    = models.SlugField(max_length= 100, unique=True)
    category                = models.ForeignKey(Category, on_delete=models.CASCADE)
   

    class Meta:
        ordering            = ['category']
        verbose_name        = 'Sub-Category'
        verbose_name_plural = 'Sub-Categories'

   
    def __str__(self): 
        return self.name

