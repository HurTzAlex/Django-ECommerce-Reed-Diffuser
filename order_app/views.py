from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required   # ต้องมีการ Login ก่อนถึงจะเข้าหน้า order.html ได้

# order หรือ การสั่งซื้อสินค้า จะต้อง models import Product, Cart, CartItem, Order and OrderDetail ด้วย
from products_app.models import Product         # ดึง Product มาเพื่อตัด Stock สินค้า
from cart_app.models import Cart, CartItem      # Cart ตะกร้าสินค้า, CartItem สินค้าในตะกร้า
from order_app.models import Order, OrderDetail # Order สะ้งซื้อสินค้า, OrderDetail รายละเอียดการสั่งซื้อสินค้า

# create_cart_id ใช้ในการดึงไอดีของตะกร้าสินค้านั้นๆ มาใช้งาน
from cart_app.views import create_cart_id


# คำสั่งซื้อสินค้า
@login_required(login_url="/login")
def order(request):
    
    if request.method == "POST":
        
        # fname, phone, email and address เอามาจาก form > input > name ของชื่อนั้นๆ จาก order.html
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        address = request.POST['address']
        
        cart = Cart.objects.get(cart_id=create_cart_id(request), customer=request.user)
        cartItem = CartItem.objects.filter(cart=cart)   # ตัวแปร cart = (object) cart
        # cartItem เอามาใช้คำนวณผลรวมหาผลรวมที่จะเก็บลงในใบสั่งซื้อสินค้า
        
        total = 0
        # total = 0 : เก็บยอดรวมของสินค้าทั้งหมด โดยต้องใช้ 0
        
        for item in cartItem:
            total += (item.product.price * item.quantity)
            
        # สร้างใบสั่งซื้อสินค้า
        order = Order.objects.create(
            fullname = fullname,
            phone = phone,
            address = address,
            total = total,
            customer = request.user
        )
        order.save()
        
        # บันทึกรายการสั่งซื้อและตัดสต๊อกสินค้า
        for item in cartItem:
            order_detail = OrderDetail.objects.create(
                product = item.product.name,
                quantity = item.quantity,
                price = item.product.price,
                order = order
            )
            order_detail.save()
            
            # ตัดสต๊อก เมื่อสินค้าได้ถูกซื้อไปแล้ว
            product = Product.objects.get(pk=item.product.id)
            product.stock = int(item.product.stock - order_detail.quantity)
            product.save()
            item.delete()
        
        cart.delete()
        return render(request, 'orderComplete.html')
        
    else:
        return render(request, 'order.html')
        

# ประวัติการซื้อสินค้า
@login_required(login_url="/login")
def orderHistory(request):
    orders = Order.objects.filter(customer = request.user)
    
    return render(request, 'orderHistory.html', {'orders': orders})


# order Detail รายละเอียดรายการคำสั่งซื้อ
@login_required(login_url="/login")
def orderDetail(request, order_id):
    
    order = Order.objects.get(pk=order_id)      # ดึง ID จากคลาส Order 
    
    if order.customer == request.user:      # ทำการตรวจสอบว่าคนที่เรียกดูข้อมูลเป็นเจ้าของใบสั่งซื้อนั้นจริงๆ หรือไม่
        order_items = OrderDetail.objects.filter(order = order)      # ดึงข้อมูล OrderDetail ตามข้อมูล order ที่ส่งมา
        return render(request, 'orderDetail.html', {'order': order, 'order_items': order_items})
        
    
    else:
        return redirect('/orderHistory')
    