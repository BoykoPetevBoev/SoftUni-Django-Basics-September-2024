from django.contrib import admin
from django.urls import path, include
from workshop_petstagram.pets_app import views

urlpatterns = [
    path('add/', views.PetAddPage.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailsPage.as_view(), name='pet-details'),
        path('edit/', views.PetEditPage.as_view(), name='pet-edit'),
        path('delete/', views.PetDeletePage.as_view(), name='pet-delete'),
    ])),
]
