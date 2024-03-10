from django.db import models

from django.contrib.auth.models import User
# django.contrib.auth.models import User ใช้สำหรับเก็บข้อมูลผู้ใช้งาน

from products_app.models import Product 
# ดึงข้อมูลโมเดล จากคลาส Product (ที่เก็บข้อมูลสินค้า)


# Cart เก็บโมเดลส์ Cart_ID & Customer 
class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # Customer คือ ForienKey ที่เชื่อมโยงกับ User ที่เก็บข้อมูลผู้ใช้งาน ซึ่งแสดงถึงผู้ที่เป็นเจ้าของตะกร้าสินค้า
    # on_delete=models.CASCADE คือ ถ้าผู้ใช้งานถูกลบออก ข้อมูลสินค้าในตะกร้าก็จะถูกลบเช่นกัน
    
    def __str__(self):
        return self.customer.username
    # เปลี่ยน Object ให้เป็น String เดิม admin > Carts จะแสดง Cart Object(1)
    # แปลง Cart Object(1) > เป็นชื่อของ username (User) นั้นๆ 
    # customer เก็บค่าของ User ค่าจึงเป็น self.customer.username
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.product.name + " : " + str(self.quantity)
    # แปลง Object ให้เป็น String
    # product เชื่อมโยงกับ model Product
    # เช็คชื่อสินค้า, ไอดีตะกร้าสินค้า และจำนวนสินค้า : return f"{self.product.name} in cart {self.cart.cart_id} - Quantity: {self.quantity}"
    # จากการแปลง Object เป็น string และจำนวนสินค้าอย่าลืมแปลงเป็น Integer : str(self.quantity)


    # เพิ่มฟังก์ชั่น ราคารวมย่อยของสินค้าแต่ละรายการ
    def sub_total(self):
        return self.product.price * self.quantity
    # product เข้าถึงฟิลด์ราคา price, quantity อ้างอิงจากฟิลด์ quantity

# ไว้จำหน้านี้ใหม่ part 40. Cart&CartItem