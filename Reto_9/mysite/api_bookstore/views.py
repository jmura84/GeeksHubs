from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer, UserSerializer
from .models import Api_Author, Api_Book, User

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Api_Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Api_Book.objects.all().order_by('id')
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer