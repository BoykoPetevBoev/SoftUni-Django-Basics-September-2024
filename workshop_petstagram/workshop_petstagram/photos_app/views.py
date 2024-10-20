from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from workshop_petstagram.photos_app.models import Photo
from workshop_petstagram.photos_app import forms
from workshop_petstagram.common_app.forms import CommentForm


class PhotoAddPage(CreateView):
    model = Photo
    form_class = forms.PhotoAddForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')
    

class PhotoEditPage(UpdateView):
    model = Photo
    form_class = forms.PhotoEditForm
    template_name = 'photos/photo-edit-page.html'
    def get_success_url(self) -> str:
        return reverse_lazy('photo-details', kwargs={
             'pk': self.kwargs['pk'], 
        })
        

class PhotoDetailsPage(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm()
        return context


def photo_delete(request, pk):
    Photo.objects.get(pk=pk).delete()
    return redirect('home')


# def photo_add(request):
#     form = forms.PhotoAddForm(request.POST or None, request.FILES or None)
    
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('home')
        
#     context = {
#         "form": form
#     }
#     return render(request, 'photos/photo-add-page.html', context)


# def photo_details(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     comments = photo.comment_set.all()
#     likes = photo.like_set.all()
#     comment_form = CommentForm()

    
#     context = {
#         "photo": photo,
#         "comments": comments,
#         "likes": likes,
#         "comment_form": comment_form

#     }
#     return render(request, 'photos/photo-details-page.html', context)


# def photo_edit(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     form = forms.PhotoEditForm(request.POST or None, request.FILES or None)
    
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('photo-details', pk)

#     context = {
#         "form": form,
#         "photo": photo
#     }
#     return render(request, 'photos/photo-edit-page.html', context)

