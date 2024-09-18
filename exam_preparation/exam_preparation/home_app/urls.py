from django.urls import path
from exam_preparation.home_app import views

urlpatterns = [
    path('', views.index, name='home')
]