from django.db import models
from django.contrib.auth.models import User     # customer(FK) เชื่อมโยงกับ User ต้อง import User มาด้วย


# Order Model โมเดลใบสั่งซื้อสินค้า
# fullname - CharField
# phone - CharField
# address - CharField
# total - DecimalField
# created - DateTimeField
# customer(FK) - User
class Order(models.Model):
    fullname = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)           
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # ตัวแปร customer(FK) เชื่อมโยงกับ User ต้อง import User มาด้วย
    

# Order#1 (ออเดอร์ไอดี 1)
# เก็บชื่อ, เบอร์, ที่อยู่, ยอดชำระ, ชื่อลูกค้า(FK ที่เชื่อมกับ User)


# Order Detail Model โมเดลรายการสั่งซื้อสินค้า
# product - CharField
# price - DecimalField
# quantity - IntegerField
# created - DateTimeField
# order(FK) - Order
class OrderDetail(models.Model):
    product = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)    # ตัวแปร order(FK) เชื่อมโยงกับโมเดล ของ class Order (ด้านบน)

# OrderDetail เก็บรายละเอียดสินค้า
# product หรือ ออเดอร์ของ User, สินค้าที่ซื้อ, ราคาสินค้า, จำนวนของสินค้า, วันและเวลาที่ซื้อ


# max_length : การเก็บข้อมูลตัวเลขหรือตัวอักษรที่มีความยาวไม่เกิน (ใส่ค่าที่ต้องการเช่น 255, 1000)
# max_digits : หลัก, decimal_place : ทศนิยม 2 ตำแหน่ง
# auto_now_add : ทำการบันทึกเวลาที่ข้อมูลถูกสร้างขึ้นโดยอัตโนมัติ
# on_delete=models.CASCADE : เมื่อวัตถุที่เชื่อมโยงกับ FK ถูกลบออกจากฐานข้อมูล(DataBase) วัตถุที่เชื่อมโยงนั้นๆ จะถูกลบไปด้วย(cascading deletion)

    def sub_total(self):
        return self.price * self.quantity