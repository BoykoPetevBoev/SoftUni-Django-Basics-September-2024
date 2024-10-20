from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from workshop_petstagram.pets_app.models import Pet
from workshop_petstagram.pets_app import forms
from workshop_petstagram.common_app.forms import CommentForm


class PetAddPage(CreateView):
    model = Pet
    # queryset = Pet.objects.all()
    form_class = forms.PetAddForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})
    

class PetDetailsPage(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = context['pet'].photo_set.all()
        context['comment_form'] = CommentForm()
        return context
    

class PetEditPage(UpdateView):
    model = Pet
    form_class = forms.PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    
    def get_success_url(self) -> str:
        return reverse_lazy('pet-details', kwargs={
             'username': self.kwargs['username'], 
             'pet_slug': self.kwargs['pet_slug'],
        })


class PetDeletePage(DeleteView):
    model = Pet
    form_class = forms.PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('progile-details', kwargs={'pk': 1})

    def get_initial(self):
        return self.objects().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs

# def pet_add(request):
#     form = forms.PetAddForm(request.POST or None)
    
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('profile-details', pk=1)
        
#     context = {
#         "form": form
#     }
#     return render(request, 'pets/pet-add-page.html', context)


    
# def pet_edit(request, username, pet_slug):
#     pet = Pet.objects.get(slug = pet_slug)
#     form = forms.PetEditForm(request.POST or None, instance=pet)
    
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('pet-details', username, pet_slug)
   
#     context = {
#         "form": form,
#         "pet": pet
#     }
#     return render(request, 'pets/pet-edit-page.html', context)



# def pet_delete(request, username, pet_slug):
#     pet = Pet.objects.get(slug = pet_slug)
#     form = forms.PetDeleteForm(instance=pet)
    
#     if request.method == "POST":
#         pet.delete()
#         return redirect('progile-details', pk=1)

#     context = {
#         "form": form,
#         "pet": pet
#     }
#     return render(request, 'pets/pet-delete-page.html', context)



# def pet_details(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     photos = pet.photo_set.all()
#     comment_form = CommentForm()

#     contect = {
#         "pet": pet,
#         "photos": photos,
#         "comment_form": comment_form
#     }
#     return render(request, 'pets/pet-details-page.html', contect)

