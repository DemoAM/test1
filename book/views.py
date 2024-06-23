from rest_framework import viewsets
from rest_framework.views import APIView
from.serializer import BookSerializer
from .models import Book

class BookApi(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['post']
