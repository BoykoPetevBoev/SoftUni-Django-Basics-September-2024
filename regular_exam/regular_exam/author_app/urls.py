from django.urls import include, path

from regular_exam.author_app.views import  CreateAuthorPage, DetailsAuthorPage, EditAuthorPage, DeleteAuthorPage

urlpatterns = [
     path('create/', CreateAuthorPage.as_view(), name='create-author'),
     path('details/', DetailsAuthorPage.as_view(), name='details-author'),
     path('edit/', EditAuthorPage.as_view(), name='edit-author'),
     path('delete/', DeleteAuthorPage.as_view(), name='delete-author'),
]
