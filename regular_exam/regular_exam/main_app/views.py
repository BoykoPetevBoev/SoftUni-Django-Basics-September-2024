from django.shortcuts import render
from django.views.generic import ListView
from regular_exam.post_app.models import Post
from regular_exam.author_app.models import Author
from regular_exam.author_app.mixins import AuthorMixin

def index(request):
    context = {
        "author": Author.objects.first()
    }
    return render(request, 'main/index.html', context)


class DashboardPage(AuthorMixin, ListView):
    model = Post
    template_name = 'main/dashboard.html'
    context_object_name = 'posts'
