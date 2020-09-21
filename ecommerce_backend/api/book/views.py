from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer, BookGenresSerializer


class BookView():
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateView(BookView, generics.ListCreateAPIView):
    pass


class BookRetrieveUpdateDestroyView(BookView, generics.RetrieveUpdateDestroyAPIView):
    pass


class BookGenresView(APIView):
    def get(self, request):
        serializer = BookGenresSerializer({"genres": {genre[0]: genre[-1] for genre in Book.GENRES}})
        return Response(serializer.data, status=status.HTTP_200_OK)
