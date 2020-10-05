from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer


class OrderView():
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListCreateView(OrderView, generics.ListCreateAPIView):
    pass


class OrderRetrieveUpdateDestroyView(OrderView, generics.RetrieveUpdateDestroyAPIView):
    pass


class MyCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)
