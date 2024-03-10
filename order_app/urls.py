from django.urls import path
from order_app import views

urlpatterns = [
    path('order', views.order, name="order"),
    path('orderHistory', views.orderHistory),
    path('order/<int:order_id>', views.orderDetail, name="orderDetail")
]