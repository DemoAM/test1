# serializers.py
from rest_framework import serializers
from .models import Book, Author, Category, Cart, CartItem, User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("id", "book", "quantity")


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"


class SignINSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

        def validate(self, data):
            email = data["email"]
            password = data["password"]
            if not email or not password:
                raise serializers.ValidationError("Email and password are required")
            user = authenticate(username=email, password=password)
            if user is None:
                raise AuthenticationFailed("Invalid credentials, please try again.")

            if not user.is_active:
                raise AuthenticationFailed("User account is disabled.")

            data["user"] = user
            return data
