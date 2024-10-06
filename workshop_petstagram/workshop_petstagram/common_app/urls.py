from django.contrib import admin
from django.urls import path, include

from workshop_petstagram.common_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
]
