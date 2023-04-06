from django.shortcuts import render
from rest_framework import generics, permissions
from .models import AlbumReview
from .serializers import AlbumReviewSerializer


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
