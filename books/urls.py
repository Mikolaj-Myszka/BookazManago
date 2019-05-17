from django.urls import path
from . import views


urlpatterns = [
    path('books', views.list_of_books, name='books')
]