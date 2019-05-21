from django.urls import path
from . import views


urlpatterns = [
    path('add-book-api', views.addbookapi, name='addbookapi')
]