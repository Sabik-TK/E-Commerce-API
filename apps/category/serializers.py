from . models import Category,SubCategory
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields ='__all__'
        
class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields ='__all__'
    


