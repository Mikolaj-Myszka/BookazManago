from django.shortcuts import render
import requests

from books.models import Book

def addbookapi(request):

    context = {}

    if request.method == "POST":
        keywords = request.POST.get('keywords')
        print(keywords)

        
        url = 'https://www.googleapis.com/books/v1/volumes?q={}'
        #keywords = 'Hobbit'
        
        r = requests.get(url.format(keywords)).json()
        #print(r.text)

        if 'title' in r['items'][0]['volumeInfo']:
            title = r['items'][0]['volumeInfo']['title']
            print("Title is: " + title)
        else:
            title = "No title"

        if 'authors' in r['items'][0]['volumeInfo']:
            author = r['items'][0]['volumeInfo']['authors'][0]
            print("author is: " + author)
        else:
            author = "No author"

        if 'description' in r['items'][0]['volumeInfo']:
            description = r['items'][0]['volumeInfo']['description']
            print("description is: " + description)
        else:
            description = "No description"

        if 'categories' in r['items'][0]['volumeInfo']:
            category = r['items'][0]['volumeInfo']['categories'][0]
            print("category is: " + category)
        else:
            category = "No category"

        
        book_fields = {
            'title': title,
            'author': author,
            'description': description[0:300] + '...', #r['items'][0]['volumeInfo']['description'],
            'category': category
            }
        print(book_fields)

        Book.objects.create(**book_fields)
        
        context = {
            'book_fields': book_fields
        }
        


    return render(request, 'addbookapi/addbookapi.html', context)
