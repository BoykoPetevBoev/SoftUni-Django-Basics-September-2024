from django.contrib import admin
from exam_preparation.album_app.models import Album

# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
