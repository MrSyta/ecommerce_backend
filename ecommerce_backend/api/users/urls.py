from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, UserLoginView, UserLogoutView, UserMeView

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
    path('users/login/', UserLoginView.as_view()),
    path('users/logout/', UserLogoutView.as_view()),
    path('users/me/', UserMeView.as_view())
]
