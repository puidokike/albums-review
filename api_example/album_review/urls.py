from django.urls import path
from .views import AlbumReviewList

urlpatterns = [
    path('albums', AlbumReviewList.as_view()),
]