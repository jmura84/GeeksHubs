from rest_framework import serializers

from .models import Api_Author, Api_Book, User

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Api_Author
        fields = ('id', 'name', 'created_date', 'added_by_id')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Api_Book
        fields = ('id', 'title', 'description', 'created_date', 'added_by_id', 'author_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'surname')