from django.shortcuts import render

from .models import Book

def list_of_books(request):
    listing = Book.objects.order_by('-added_date')
    context = {
        'listings': listing
    }
    return render(request, 'books/listings.html', context)
