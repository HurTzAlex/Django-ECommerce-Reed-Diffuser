from django.urls import path
from cart_app import views

urlpatterns = [
    path('cart', views.cart, name="cart"),
    path('cart/add/<int:product_id>', views.addCart, name="addCart"),
    path('cart/remove/<int:product_id>', views.removeCart, name="removeCart")
]
# นำ path urls ของ cart_app ไปใส่ใน part urls ของ main_web 