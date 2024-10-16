from django.urls import include, path
from templates_basics.posts_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dash'),
    path('add-post/', views.add_post, name='add-post'),
    path('<int:pk>/', include([
        path('edit/', views.post_edit, name='edit-post'),
        path('delete/', views.post_delete, name='post-delete'),
        path('details/', views.post_details, name='post-details'),
    ])),
]