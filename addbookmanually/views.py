from django.shortcuts import render

from .forms import BookForm


def addbookmanually(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()

    context = {
        'form': form
    }
    return render(request, 'addbookmanually/addbookmanually.html', context)
