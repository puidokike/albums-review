from django.contrib import admin
from .models import Band, Song, Album, AlbumReview, AlbumReviewComment, AlbumReviewLike

admin.site.register(Band)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(AlbumReviewComment)
admin.site.register(AlbumReview)
admin.site.register(AlbumReviewLike)
