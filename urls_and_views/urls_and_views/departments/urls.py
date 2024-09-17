from django.contrib import admin
from django.urls import path, include

from urls_and_views.departments import views 

urlpatterns = [
    path('', views.index, name="home"),
    
    path('department/', views.redirect_to_frontend_department),
    path('softuni/', views.redirect_to_softuni),
    path('home/', views.redirect_to_home, name='redirect-home'),
    path('not-found/', views.view_404),
    
    path('<int:pk>/', include([
        path('', views.view_with_pk, name='department'),
        path('<slug:slug>/', views.view_with_slug),
    ])),
   
    path('<str:param>/', views.view_with_name),
    path('<path:param>/', views.view_with_path),
]
