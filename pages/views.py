from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book


def home(request):
    home_listing = Book.objects.order_by('-added_date')[:3]
    context = {
        'listings': home_listing
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
