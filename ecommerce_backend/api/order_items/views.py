from rest_framework import generics

from .models import OrderItem
from .serializers import OrderItemSerializer


class OrderItemView():
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemListCreateView(OrderItemView, generics.ListCreateAPIView):
    pass


class OrderItemRetrieveUpdateDestroyView(OrderItemView, generics.RetrieveUpdateDestroyAPIView):
    pass
