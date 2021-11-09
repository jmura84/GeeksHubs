from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        # id = serializers.ReadOnlyField()
        fields = ('id', 'name', 'alias')
