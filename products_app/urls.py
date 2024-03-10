# urls.py จะทำงานสัมพันธ์กับ views.py ใน product_app
from django.urls import path
from products_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('BestSellerProduct/Details/<int:id>', views.productBestDetail, name = 'productBestDetail'),
    path('AllProduct/Details/<int:id>', views.all_products, name = 'all_products'),
    path('search/', views.search, name = 'search')
]