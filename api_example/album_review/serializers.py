from rest_framework import serializers
from .models import AlbumReview


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'album_id', 'content', 'score']