from rest_framework import serializers
from .models import Book, Category, Author, Cart
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        author = data.get("author")
        title = data.get("title")
        writer = Book.objects.filter(author=author).first()
        book_writer = writer.author
        name = Book.objects.filter(title=title).first()
        book_name = name.title

        if author == book_writer:
            if book_name == title:
                raise serializers.ValidationError("This book is already with same author")

        return data
