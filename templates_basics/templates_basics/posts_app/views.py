from datetime import datetime
from django.shortcuts import redirect, render
from templates_basics.posts_app.forms import PersonForm, PostForm, PostEditForm, PostDeleteForm, SearchForm
from templates_basics.posts_app.models import Post

def index(request):

    form_data = PersonForm(request.POST or None)
    
    context = {
        "form": form_data
    }

    return render(request, 'base.html', context)


def dashboard(request):
    form = SearchForm(request.GET or None)
    posts = Post.objects.all()
    
    if request.method == "GET":
        if form.is_valid():
            search = form.cleaned_data['search']
            posts = posts.filter(title__icontains=search)
            
    context = {
        "posts": posts,
        "form": form
    }
    return render(request, 'posts_app/posts.html', context)


def add_post(request):
    form = PostForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("dash")
    
    context = {
        "form": form
    }

    return render(request, "posts_app/add-post.html", context)    

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    print(post)
    context = {
        "post": post
    }
    return render(request, "posts_app/details-post.html", context)    


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-details', post.pk)
    else:
        form = PostEditForm(instance=post)
    
    context = {
        "form": form,
        "post": post
    }
    return render(request, "posts_app/edit-post.html", context)    


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)
  
    if request.method == 'POST':
        post.delete()
        return redirect('dash')
  
    context = {
        "form": form,
        "post": post
    }
    return render(request, "posts_app/delete-post.html", context)    