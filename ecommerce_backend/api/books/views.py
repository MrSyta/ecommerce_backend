from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from .models import Book
from .serializers import BookSerializer


class BookView():
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateView(BookView, generics.ListCreateAPIView):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ["release_date", "price"]


class BookRetrieveUpdateDestroyView(BookView, generics.RetrieveUpdateDestroyAPIView):
    pass


class BookGenresView(APIView):
    def get(self, request):
        genres = {genre[0]: genre[-1] for genre in Book.GENRES}
        return Response(genres, status=status.HTTP_200_OK)
