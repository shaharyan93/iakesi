from rest_framework import serializers

from .models import *


__all__ = [
    'SeriesSerializer',
    'SeriesImageSerializer'
]


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    cover_image = serializers.ReadOnlyField(source='image_path')

    class Meta:
        model = Series
        fields = ('id', 'name', 'cover_image', 'description', 'anilist_id', 'last_modified')


class SeriesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('image', )
