from django.db import models
from datetime import datetime

class Book(models.Model):
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    added_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title + " - " + self.author
