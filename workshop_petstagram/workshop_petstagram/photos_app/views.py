from django.shortcuts import redirect, render

from workshop_petstagram.photos_app.models import Photo
from workshop_petstagram.photos_app import forms
from workshop_petstagram.common_app.forms import CommentForm

# Create your views here.

def photo_add(request):
    form = forms.PhotoAddForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {
        "form": form
    }
    return render(request, 'photos/photo-add-page.html', context)


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all()
    likes = photo.like_set.all()
    comment_form = CommentForm()

    
    context = {
        "photo": photo,
        "comments": comments,
        "likes": likes,
        "comment_form": comment_form

    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = forms.PhotoEditForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {
        "form": form,
        "photo": photo
    }
    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    Photo.objects.get(pk=pk).delete()
    return redirect('home')