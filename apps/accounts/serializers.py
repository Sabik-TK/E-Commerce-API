from . models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Account
        fields = '__all__'

        fields = ['id','username','email','mobile','is_active','password']
        extra_kwargs={'email':{'required':True},'is_active':{'read_only' : True}}

    def create(self, validated_data):
        user = Account(
                email      = validated_data['email'],
                mobile     = validated_data['mobile'],
                
            )
        user.set_password(validated_data['password'])
        user.save()
        return user
