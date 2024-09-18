
from django.urls import path
from exam_preparation.album_app import views

urlpatterns = [
    path('add/', views.album_add, name='album-create'),
    path('<int:pk>/details/', views.album_details, name='album-details'),
    path('<int:pk>/edit/', views.album_edit, name='album-edit'),
    path('<int:pk>/delete/', views.album_delete, name='album-delete'),
]