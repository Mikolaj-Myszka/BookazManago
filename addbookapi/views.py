from django.shortcuts import render
import requests


def addbookapi(request):
    text = 'some text'
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'
    keyword = 'Hobbit'
    
    r = requests.get(url.format(keyword)).json()
    #print(r.text)

    book_fields = {
        'title': r['items'][0]['volumeInfo']['title'],
        'author': r['items'][0]['volumeInfo']['authors'][0],
        'description': 'Some description here', #r['items'][0]['volumeInfo']['description'],
        'category': r['items'][0]['volumeInfo']['categories'][0]
        }
    print(book_fields)
    
    """
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()
    """
    context = {
        'book_fields': book_fields
    }
    

    return render(request, 'addbookapi/addbookapi.html', context)
