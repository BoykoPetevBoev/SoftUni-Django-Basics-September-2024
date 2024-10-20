from django.shortcuts import redirect, render

from workshop_petstagram.pets_app.models import Pet
from workshop_petstagram.pets_app import forms
from workshop_petstagram.common_app.forms import CommentForm

# Create your views here.

def pet_add(request):
    form = forms.PetAddForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('profile-details', pk=1)
        
    context = {
        "form": form
    }
    return render(request, 'pets/pet-add-page.html', context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug = pet_slug)
    form = forms.PetEditForm(request.POST or None, instance=pet)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)
   
    context = {
        "form": form,
        "pet": pet
    }
    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug = pet_slug)
    form = forms.PetDeleteForm(instance=pet)
    
    if request.method == "POST":
        pet.delete()
        return redirect('progile-details', pk=1)

    context = {
        "form": form,
        "pet": pet
    }
    return render(request, 'pets/pet-delete-page.html', context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    photos = pet.photo_set.all()
    comment_form = CommentForm()

    contect = {
        "pet": pet,
        "photos": photos,
        "comment_form": comment_form
    }
    return render(request, 'pets/pet-details-page.html', contect)

