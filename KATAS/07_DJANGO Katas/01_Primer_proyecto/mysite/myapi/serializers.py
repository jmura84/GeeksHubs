from rest_framework import serializers
from .models import Author, Book
# from .models import Hero

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'added_by', 'created_date')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author', 'added_by', 'created_date')

# class HeroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Hero
#         # id = serializers.ReadOnlyField()
#         fields = ('id', 'name', 'alias')
