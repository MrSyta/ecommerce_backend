from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly


class BookView():
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]


class BookListCreateView(BookView, generics.ListCreateAPIView):
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['genre']
    search_fields = ['title', 'author']
    ordering_fields = ["release_date", "price"]


class BookRetrieveUpdateDestroyView(BookView, generics.RetrieveUpdateDestroyAPIView):
    pass


class BookGenresView(APIView):
    def get(self, request):
        genres = {genre[0]: genre[-1] for genre in Book.GENRES}
        return Response(genres, status=status.HTTP_200_OK)
