from django.shortcuts import render

# อิมพอร์ทโมเดล Product ใน products_app 
from products_app.models import Product
from products_app.models import ProductPromotion

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    
    # นำข้อมูล isTrending สินค้าขายดีหรือยอดนิยมมาแสดง โดยเรียก .filter กรอง isTrending
    productBestSeller = Product.objects.filter(isTrending=True)
    
    # นำรูปโปรฯ มาแสดง โดยเรียก .all
    productPromotions = ProductPromotion.objects.all()
    
    # กำหนด all_products ที่จะใช้กับ Paginator และกำหนดการเรียงสินค้าด้วยชื่อ .order_by('name')
    all_products = Product.objects.all().order_by('name')
    
    # Paginator
    page = request.GET.get('page')
    paginator = Paginator(all_products, 8)
    
    all_products = paginator.get_page(page)
    
    return render(request, 'index.html', {'productBestSeller': productBestSeller, 'productPromotions': productPromotions, 'all_products': all_products})


# ดึง Best Seller
def productBestDetail(request, id):
    
    # ดึงข้อมูล id หรือ pk จากหน้าเพจ BestSeller 
    productBest = Product.objects.get(pk = id)
    
    
    return render(request, 'product.html', {'productBest': productBest})


# ดึง All Products
def all_products(request, id):
    
    # ดึงข้อมูล id หรือ pk จากหน้าเพจ Products 
    products = Product.objects.get(id = id)

    return render(request, 'all_products.html', {'products': products})


# Search
def search(request):
    
    
    
    if request.method == "POST":
        searched = request.POST['searched']
        products_all = Product.objects.filter(name__contains = searched)
        return render(request, 'search.html', {'searched': searched, 'products_all': products_all})
    
    else:
        return render(request, 'search.html')