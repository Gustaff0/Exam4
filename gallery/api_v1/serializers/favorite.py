from rest_framework import serializers
from webapp.models import Favorites

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['id', 'photo', 'user']
        read_only_fields = ['id', 'order']