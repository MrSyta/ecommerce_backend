from django.urls import path
from .views import OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view()),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view()),
]
