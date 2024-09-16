import django_introduction.todo_app.views as views
from django.urls import path

urlpatterns = [
    path('', views.index),
]
