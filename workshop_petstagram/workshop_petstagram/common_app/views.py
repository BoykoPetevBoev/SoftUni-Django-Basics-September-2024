from django.views.generic import ListView

from django.shortcuts import redirect, render, resolve_url
from pyperclip import copy

from workshop_petstagram.photos_app.models import Photo
from workshop_petstagram.common_app.models import Like, Comment
from workshop_petstagram.common_app.forms import CommentForm, SearchForm

# Create your views here.

class HomePage(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_py = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')
        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)
        return queryset



# def home(request):
#     all_photos = Photo.objects.all()
#     comment_form = CommentForm()
#     search_form = SearchForm(request.GET)

#     if search_form.is_valid():
#         all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

#     context = {
#         "all_photos": all_photos,
#         "search_form": search_form,
#         "comment_form": comment_form,
#     }
#     return render(request, 'common/home-page.html', context)


def like(request, photo_id: int):
    like = Like.objects.filter(
        to_photo_id=photo_id
    ).first()
     
    if like:
        like.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()
        
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


def share(request, photo_id: int):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')
    
    
def comment(request, photo_id: int):
    if request.method == "POST":
        photo = Photo.objects.get(pk=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')
