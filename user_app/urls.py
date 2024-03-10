# urls.py จะทำงานสัมพันธ์กับ views.py ใน user_app
from django.urls import path
from user_app import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")
]