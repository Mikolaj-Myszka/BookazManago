from django.urls import path
from . import views


urlpatterns = [
    path('add-book-manually', views.addbookmanually, name='addbookmanually')
]