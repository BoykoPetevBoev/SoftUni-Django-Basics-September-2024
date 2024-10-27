from django.urls import include, path

from regular_exam.post_app.views import DetailsPostPage, CreatePostPage, EditPostPage, DeletePostPage

urlpatterns = [
    path('create/', CreatePostPage.as_view(), name='create-post'),
    path('<int:pk>/', include([
        path('details/', DetailsPostPage.as_view(), name='details-post'),
        path('edit/', EditPostPage.as_view(), name='edit-post'),
        path('delete/', DeletePostPage.as_view(), name='delete-post'),
    ])),     
]
