from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
]
