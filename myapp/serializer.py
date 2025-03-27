from rest_framework import serializers
from django.contrib.auth.models import User
import re

from .models import CustomerInfo , UserMessages
from django.contrib.auth.password_validation import validate_password



class UserSerializer(serializers.ModelSerializer):
    class Meta: 

        model = User
        fields= ["id" , "email" , "password"]
        extra_kwargs = {'password': {'write_only' : True}}

    def validate_password(self , value):
        if len(value)< 8:
            raise serializers.ValidationError("Password must be atleast greater than 8 characters")
        if not re.search(r"[A-Z]" , value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter ")
        if not re.search(r"[a-z]" , value):
            raise serializers.ValidationError("Password must contain atleast one lowercase letter")
        if not re.search(r"\d", value):
            raise serializers.ValidationError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise serializers.ValidationError("Password must contain at least one special character")
        try:
            print("Validating password...")
            validate_password(value)
        except Exception as e:
            print("Validations error:" , e)
            raise serializers.ValidationError(str(e))
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['email'],
            email = validated_data['email'],
            password= validated_data['password']
        )
    
        return user
    
#helps user to make images and upload a message  
class UserMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMessages
        fields = ['user' , 'id' , 'message' , 'images']

    def validate(self, data):
        if not data.get('message') and not data.get('images'):
            raise serializers.ValidationError("Either message or image must be provided.")
        return data
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


# Customer details serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomerInfo
        fields= ["id" , "name" , "email" , "phone" , "message" , "created_at"]

