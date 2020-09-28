import os
import uuid
from django.db import models


class Book(models.Model):

    GENRES = [
        ("B", "Biografia"),
        ("F", "Fantasy"),
        ("H", "Historia"),
        ("K", "Komiks"),
        ("P", "Poradnik"),
        ("I", "Inne"),
        ]

    def generate_filename(self, filename):
        PATH = "book_covers/"
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return os.path.join(PATH, filename)

    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=1, choices=GENRES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    cover = models.ImageField(upload_to=generate_filename)

    class Meta:
        ordering = ['title']
        db_table = 'books'

    def __str__(self):
        return self.title
