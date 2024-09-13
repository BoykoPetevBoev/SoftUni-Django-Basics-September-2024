import djangoIntroduction.todo_app.views as views
from django.urls import path

urlpatterns = [
    path('', views.index),
]
