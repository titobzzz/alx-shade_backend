from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User

class UserRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type" : "password"})

    class Meta:
        model= User
        fields=[
            "id",
            "date_of_birth",
            "bio",
            "full_name",
            "username",
            "email",
            "password",
            "avatar"
        ]

    def create(self, validated_data):
        """
        Create and return a new user instance, properly handling the password.
        """
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"]
        )
        print("serializable")
        return user

class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        fields="__all__"
