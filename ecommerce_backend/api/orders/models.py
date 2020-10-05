from django.db import models
from ..users.models import User
from ..books.models import Book


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)


def __str__(self):
    return str(self.id)