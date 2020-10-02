from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


class UserView():
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListCreateView(UserView, generics.ListCreateAPIView):
    def post(self, request, format=None):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()

            token = ObtainAuthToken().post(request)
            user_data = user.data
            user_data['token'] = token.data['token']

            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateDestroyView(UserView, generics.RetrieveUpdateDestroyAPIView):
    pass


class UserMeView(APIView):
    def get(self, request, format=None):
        if my_id := request.user.id:
            me = User.objects.get(id=my_id)
            return Response(UserSerializer(me).data, status=status.HTTP_200_OK)
        else:
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)


class UserLoginView(APIView):
    serializer_class = AuthTokenSerializer

    def post(self, request):
        return ObtainAuthToken().post(request)


class UserLogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
