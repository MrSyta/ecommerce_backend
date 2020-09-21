from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView, BookGenresView

urlpatterns = [
    path('book/', BookListCreateView.as_view()),
    path('book/<int:pk>/', BookRetrieveUpdateDestroyView.as_view()),
    path('book/genres/', BookGenresView.as_view())
]
