from django.urls import path
from .views import OrderItemListCreateView, OrderItemRetrieveUpdateDestroyView

urlpatterns = [
    path('order_items/', OrderItemListCreateView.as_view()),
    path('order_items/<int:pk>/', OrderItemRetrieveUpdateDestroyView.as_view()),
]
