from django.contrib import admin
from django.urls import path, include
from workshop_petstagram.accounts_app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.profile_edit, name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete')
    ])),
]
