from django.urls import path
from exam_preparation.user_app import views

urlpatterns = [
    path('details/', views.details, name='profile-details'),
    path('delete/', views.delete, name='profile-delete'),
]