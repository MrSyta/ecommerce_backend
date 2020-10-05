from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    groups = models.ForeignKey(Group, default=2, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)

    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return self.username
