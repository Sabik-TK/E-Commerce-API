from apps.product.serializers import ProductListSerializer
from . models import MainCategory,Category
from rest_framework import serializers


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name','url')
    
class MainCategorySerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="main-category-detail")
    categories = CategoryListSerializer(read_only=True, many=True)

    class Meta:
        model = MainCategory
        fields = ('id','category_no','url','name','thumbnail','categories')


class CategorySerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="category-detail")
    products = ProductListSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields ='__all__'