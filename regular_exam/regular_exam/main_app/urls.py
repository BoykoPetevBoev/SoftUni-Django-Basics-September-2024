from django.contrib import admin
from django.urls import path
from regular_exam.main_app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('dashboard/', views.DashboardPage.as_view(), name="dashboard"),
]