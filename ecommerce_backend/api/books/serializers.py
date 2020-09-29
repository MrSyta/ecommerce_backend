from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    genre_display = serializers.CharField(source='get_genre_display', read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
