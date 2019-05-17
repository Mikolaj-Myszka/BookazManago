from django.shortcuts import render

from .models import Book

"""
def list_of_books(request):
    listing = Book.objects.order_by('-added_date')
    context = {
        'listings': listing
    }
    return render(request, 'books/listings.html', context)
"""


def list_of_books(request):
    queryset_list = Book.objects.order_by('-added_date')

    #Author
    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            queryset_list = queryset_list.filter(author__icontains=author)

    #Title
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)
    
    #Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__icontains=category)

    context = {
        'listings': queryset_list,
        'values': request.GET
    }
    print(request.GET)
    #print(context['values']['keywords'])
    return render(request, 'books/listings.html', context)