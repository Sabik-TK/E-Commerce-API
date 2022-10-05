from django.db import models
# Create your models here.

class MainCategory(models.Model):
    name           = models.CharField(max_length= 50, unique=True)
    thumbnail      = models.ImageField(upload_to='photos/categories', blank = True)
    category_no    = models.IntegerField(unique=True)

    class Meta:
        ordering            = ['category_no']
        verbose_name        = 'Main-Category'
        verbose_name_plural = 'Main-Categories'

    def __str__(self):
        return self.name


class Category(models.Model):

    name     = models.SlugField(max_length= 100, unique=True)
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='categories')
   

    class Meta:
        ordering            = ['category']
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'

   
    def __str__(self): 
        return self.name

