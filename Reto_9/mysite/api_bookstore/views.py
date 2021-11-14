from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer
from .models import Api_Author, Api_Book

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Api_Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Api_Book.objects.all().order_by('id')
    serializer_class = BookSerializer