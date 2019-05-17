from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'added_date', 'description')
    list_per_page = 25

admin.site.register(Book, BookAdmin)