from django.http import HttpResponse
from django.shortcuts import render

from djangoIntroduction.todo_app.models import Task

# Create your views here.

def index(request):
    title_filter = request.GET.get('title_filter', '')
    
    if title_filter:
        tasks = Task.objects.filter(name__icontains=title_filter)
    else:
        tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
        'title_filter': title_filter,
    }
    
    return render(request, 'tasks/index.html', context)