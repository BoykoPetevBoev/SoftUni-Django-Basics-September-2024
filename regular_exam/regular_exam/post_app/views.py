from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from regular_exam.post_app.models import Post
from regular_exam.author_app.models import Author
from regular_exam.post_app.forms import CreatePostForm, EditPostForm, DeletePostForm
from regular_exam.author_app.mixins import AuthorMixin


class DetailsPostPage(AuthorMixin, DetailView):
    model = Post
    template_name = 'post/details-post.html'


class CreatePostPage(AuthorMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        form.instance.author = Author.objects.first()
        return super().form_valid(form)


class EditPostPage(AuthorMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'post/edit-post.html'
    success_url = reverse_lazy('dashboard')


class DeletePostPage(AuthorMixin, DeleteView):
    model = Post
    form_class = DeletePostForm
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('dashboard')
    
    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)