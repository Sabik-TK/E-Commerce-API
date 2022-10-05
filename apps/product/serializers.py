from . models import Product
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields ='__all__'

        extra_kwargs={
            
            'sold_quantity' :{'read_only':True},
            'is_available'  :{'read_only' : True},
            }
        
class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('url','name', 'price', 'thumbnail')

   
   