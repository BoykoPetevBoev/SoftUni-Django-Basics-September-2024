from django.urls import path
from templates_basics.posts_app.views import dashboard, index

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dash'),
]