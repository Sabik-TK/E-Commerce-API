from django.contrib import admin
from apps.category.models import Category, MainCategory


admin.site.register(MainCategory)
admin.site.register(Category)

