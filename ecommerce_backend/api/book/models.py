from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    cover = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['title']
        db_table = 'books'

    def __str__(self):
        return self.title
