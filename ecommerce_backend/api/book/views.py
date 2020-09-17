from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class BookView():
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateView(BookView, generics.ListCreateAPIView):
    pass


class BookRetrieveUpdateDestroyView(BookView, generics.RetrieveUpdateDestroyAPIView):
    pass
