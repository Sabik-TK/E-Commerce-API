from . models import Account
from rest_framework import serializers

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Account
        fields = '__all__'

        fields = [
            'id','url','username','email','mobile',
            'is_active','password','is_verified'
            ]

        extra_kwargs={
            'email':{'required':True},
            'is_active':{'read_only' : True},
            'is_verified':{'read_only' : True},
            }

    def create(self, validated_data):
        user = Account(

                username   = validated_data['username'],
                email      = validated_data['email'],
                mobile     = validated_data['mobile'],
                
            )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user
