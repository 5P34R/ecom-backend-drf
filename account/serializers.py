from django.db.models import fields
from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
      

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password']

        def create(self, validated_data):
            user = CustomUser.objects.create(**validated_data)
            return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            if CustomUser.objects.filter(email=email).exists():
                # breakpoint()
                user = authenticate(request=self.context['request'], email=email, password=password)
            else:
                msg = {'detail':'email is not registered',
                        'register':False
                      }
                raise serializers.ValidationError(msg)
            
            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')
        
        
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        
        data['user'] = user
        return data