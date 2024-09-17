import json
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from urls_and_views.departments.models import Department

# Create your views here.
 

def index(request):
    url = reverse("redirect-home")
    url_lazy = reverse_lazy("redirect-home")
    return HttpResponse(f"<h1>Reverse: {url} Reverse Lazy: {url_lazy}</h1>")

def view_with_name(request, *args, **kwargs):
    return HttpResponse(f"<h1>Param Page: Args:{args}, Kwargs: {kwargs}</h1>")
    
def view_with_name(request, param):
    context = {
        "param": param
    }
    return render(request, 'departments/param_template.html', context)

def view_with_pk(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return JsonResponse({"pk": department.pk})

def view_with_slug(request, pk, slug):
    return HttpResponse(f"<h1>Department slug: {slug}</h1>")

def view_with_path(request, param):
    return HttpResponse(f"<h1>Default page: {param}</h1>", content_type="text/plain")
    
def view_404(request):    
    raise Http404
    
def redirect_to_softuni(request):
    return redirect('https://softuni.bg')

def redirect_to_home(request):
    return redirect("home")

def redirect_to_frontend_department(request):
    return redirect("department", pk=1)

def reverse_view(request):
    url = reverse("redirect-home")
    url_lazy = reverse_lazy("redirect-home")
    return HttpResponse(f"<h1>Reverse: {url} Reverse Lazy: {url_lazy}</h1>")
