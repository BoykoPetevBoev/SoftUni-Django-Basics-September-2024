from django.shortcuts import render
from exam_preparation.album_app.models import Album
# Create your views here.

def album_add(request):
    return render(request, 'album-add.html')


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'album-details.html')


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'album-edit.html')


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'album-delete.html')
