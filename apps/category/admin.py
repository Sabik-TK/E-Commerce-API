from django.contrib import admin

from apps.category.models import Category, SubCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)

