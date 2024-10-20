from django.contrib import admin
from django.urls import path, include

from workshop_petstagram.common_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:photo_id>/', views.like, name='like-photo'),
    path('share/<int:photo_id>/', views.share, name='share-photo'),
    path('comment/<int:photo_id>/', views.comment, name='comment-photo'),
]
