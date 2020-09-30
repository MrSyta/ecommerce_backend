from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserView():
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListCreateView(UserView, generics.ListCreateAPIView):
    pass


class UserRetrieveUpdateDestroyView(UserView, generics.RetrieveUpdateDestroyAPIView):
    pass
