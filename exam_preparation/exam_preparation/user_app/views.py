from django.shortcuts import render

# Create your views here.

def details(request):
    return render(request, 'profile-details.html')


def delete(request):
    return render(request, 'profile-delete.html')