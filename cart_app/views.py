from django.shortcuts import render, redirect

# login_required เป็น Decorators ที่คอยตรวจสอบว่ามีการเข้าสู่ระบบแล้วหรือไม่ ถ้ายังไม่ได้เข้าสู่ระบบจะทำการ redirect ไปยังหน้า login โดยอัตโนมัติ
from django.contrib.auth.decorators import login_required

from products_app.models import Product

# สร้างตะกร้าสินค้าต้อง import cart_app models Cart
# ซื้อสินค้าต้อง import cart_app models CartItem
from cart_app.models import Cart, CartItem

# ถ้าเราจะเข้าถึงข้อมูล ตะกร้าสินค้า เราจะไปดึงข้อมูลของ "cart = request.session.session_key" 
# ถ้ายังไม่เคยซื้อสินค้าเลย จะให้ทำการสร้างตะกร้าสินค้า "cart = request.session.create()"
def create_cart_id(request):
    cart = request.session.session_key
    
    if not cart :
        cart = request.session.create()
    
    return cart

# cart หรือ ปุ่มตะกร้าจะทำการ login ก่อนถึงจะแสดง icon ตะกร้า
# @login_required ให้ทำการ login ก่อน icon cart หรือ ตะกร้า จะแสดงและสามารถหยิบสินค้าได้ แต่ถ้ายังไม่ไดทำการ login จะได้ไปยัง login_url ของ หน้าเพจ หรือ path /login
@login_required(login_url="/login")
def cart(request):
    
    # count = 0 : เก็บปริมาณสินค้าทั้งหมด
    count = 0
    
    # total = 0 : ยอดชำระเงินรวม
    total = 0
    
    try:
        
        # ดึงข้อมูลตะกร้าสินค้า โดย ไอดีตะกร้าสินค้า และ ลูกค้า ใช้เทียบกับฟิลด์ customer ในโมเดล Cart ซึ่งเป็น ForienKey ที่เชื่อมโยงกับผู้ใช้งาน User ในการกำหนดให้ตะกร้าสินค้าเป็นของผู้ใช้ที่ล็อคอินอยู่
        cart = Cart.objects.get(cart_id = create_cart_id(request), customer = request.user)
        
        # ดึงข้อมูลสินค้าในตะกร้า > ตะกร้าสินค้าต้องเป็นตะกร้าเดียวกัน cart = cart
        cart_item = CartItem.objects.filter(cart = cart)
        
        # คำนวณปริมาณสินค้า "cart_item ที่ดึงมามีสินค้าเท่าไหร่ ให้นำมาคำนวณ"
        for item in cart_item:
            
            # นำ item มาหาจำนวนของสินค้า ก็คือ quantity
            count += item.quantity
            
            # สินค้าทั้งหมด += (ราคาสินค้า คูณ จำนวนสินค้า) เช่น ราคาสินค้า 200 คูณ จำนวนสินค้า 2 ชิ้น เท่ากับ 400 เป็นต้น
            total += (item.product.price * item.quantity)
    
    # except ระบุ ยังไม่มีการสร้างตะกร้าสินค้า และ ยังไม่มีรายการสินค้า
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        cart = None
        cart_item = None
    
    return render(request, 'cart.html', {'cart_item': cart_item, 'total': total, 'count': count})


# ฟังกค์ชั่น หยิบสินค้า ลงตะกร้า
@login_required(login_url="/login")
def addCart(request, product_id):
    products = Product.objects.get(pk = product_id)
    
    # สร้างตะกร้าสินค้า ดึง create_cart_id มา จะเก็บข้อมูล รหัสตะกร้าสินค้า และ เจ้าของตะกร้าสินค้า
    
    # มีตะกร้าสินค้า
    try:
        
        # ถ้าในระบบมี session.session_key หรือ "cart = request.session.session_key" 
        cart = Cart.objects.get(cart_id = create_cart_id(request))
    
    # ไม่มีตะกร้าสินค้า
    except Cart.DoesNotExist:
        
        # ถ้าไม่มี session.session_key จะให้ทำการสร้าง session.session_create() > "cart = request.session.create()"
        # สร้างตะกร้าสินค้า เก็บไว้ในชืิ่อ cart
        cart = Cart.objects.create(
            
            # สร้างรหัสตะกร้าสินค้า
            cart_id = create_cart_id(request),
            customer = request.user
            
        )
        cart.save()
    
    # บันทึกรายการสินค้าในตะกร้า
    # ซื้อสินค้าชิ้นเดิม
    try:
        # ทำการเช็คสินค้านั้นๆ และ ตะกร้าสินค้า ถ้ามีสินค้าอยู่
        cart_item = CartItem.objects.get(
            product=products,
            cart=cart,
            )
        
        # จะทำการเพิ่มสินค้านั้นๆ
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    
    # ซื้อสินค้าใหม่ หรือ ซื้อครั้งแรก
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            
            # products ตัวแปรจาก addCart จะเก็บข้อมูลของสินค้าตัวนั้น
            product = products,
            
            # cart ที่ได้จากสร้างก่อนหน้านี้ จะเก็บข้อมูลตะกร้า
            cart = cart,
            
            # quantity กำหนดให้เป็น 1 จะเก็บข้อมูลปริมาณเริ่มต้น คือ 1 ชิ้น
            quantity = 1,
            
        )
        cart_item.save()
        
    print(cart_item)
    
    return redirect('/cart')

# ฟังก์ชั่น ลบสินค้า ในตะกร้า (ไอคอนถังขยะ)
@login_required(login_url="/login")
def removeCart(request, product_id):
    
    # ต้องดึงคำสั่ง ไอดีตะกร้าสินค้า และ ดึงผู้ใช้งานของตะกร้านั้นๆ ก็คือ user
    cart = Cart.objects.get(cart_id = create_cart_id(request), customer = request.user)
    
    # ดึงไอดีสินค้าของโมเดล Product หรือ สินค้า
    product = Product.objects.get(pk = product_id)
    
    # ดึงข้อมูลจากฐานข้อมูล CartItem โดยใช้เงื่อนไขของ cart & product ที่ได้สร้างไว้ก่อนหน้านี้
    # product & cart คือ ตัวแปรที่ระบุ สินค้า และ ตะกร้าสินค้า ที่ต้องการดึงข้อมูล
    cart_item = CartItem.objects.get(product = product, cart = cart)    # สินค้าที่ต้องการลบ
    
    cart_item.delete()
    
    return redirect('/cart')