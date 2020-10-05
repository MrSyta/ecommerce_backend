from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer


class OrderView():
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListCreateView(OrderView, generics.ListCreateAPIView):
    pass


class OrderRetrieveUpdateDestroyView(OrderView, generics.RetrieveUpdateDestroyAPIView):
    pass
