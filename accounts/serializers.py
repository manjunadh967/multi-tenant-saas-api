from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "name"]

    def create(self, validated_data):
        email=validated_data['email']
        password=validated_data['password']
        name=validated_data['name']
        
        user = User.objects.create_user(
            email=email,
            username=email,
            password=password,
            name=name
        )

        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']