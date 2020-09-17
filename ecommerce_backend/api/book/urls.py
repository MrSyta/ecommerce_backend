from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('book/', BookListCreateView.as_view()),
    path('book/<int:pk>/', BookRetrieveUpdateDestroyView.as_view())
]
