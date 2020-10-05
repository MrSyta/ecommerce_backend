from django.urls import path
from .views import OrderListCreateView, OrderRetrieveUpdateDestroyView, MyCartView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view()),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view()),
    path('my_cart/', MyCartView.as_view())
]
