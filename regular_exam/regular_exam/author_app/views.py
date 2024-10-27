from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from regular_exam.author_app.models import Author
from regular_exam.author_app.forms import CreateAuthorForm, EditAuthorForm, DeleteAuthorForm


class DetailsAuthorPage(DetailView):
    model = Author
    template_name = 'author/details-author.html'

    def get_object(self):
        return Author.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.object.posts.all()
        context['last_posts'] = posts.first()
        context['posts_number'] = len(posts)
        
        return context


class CreateAuthorPage(CreateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('dashboard')


class EditAuthorPage(UpdateView):
    model = Author
    form_class = EditAuthorForm
    template_name = 'author/edit-author.html'
    success_url = reverse_lazy('details-author')
    
    def get_object(self):
        return Author.objects.first()


class DeleteAuthorPage(DeleteView):
    model = Author
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return Author.objects.first()
