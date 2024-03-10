from django.db import models

# Superuser ID : admin, Pass : admin1234
# Create your models here.
class Product(models.Model): # เก็บข้อมูลสินค้า
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)     # max_digits 10 : จำนวนตัวเลข 10 หลัก, decimal_places 2 : ทศนิยม 2 ตำแหน่ง
    stock = models.IntegerField()       # จำนวนสินค้าในคลัง(ใส่ไว้ก่อน)
    isTrending = models.BooleanField(default=False)     # สินค้าเป็นที่นิยมหรือขายดี
    
    image = models.ImageField(upload_to='products-img', blank=True)     # เก็บภาพสินค้า, upload_to : เก็บภาพที่โฟลเดอร์ ' ', blank : ใส่ภาพหรือไม่ก็ได้
    # image field ต้องติดตั้ง pip pillow, python : pip install pillow, python3 : python3 -m pip install pillow
    

    # def __str__(self):
    #     return self.name
    # self.name แปลง Object ให้เป็น string // Terminal จะแสดง Object(ตามด้วยเลขของสินค้า) หรือ Terminal จะแสดง ชื่อสินค้า [จะใส่หรือไม่ใส่ก็ได้]

class ProductPromotion(models.Model):
    imagePromotion = models.ImageField(upload_to='products-promotion-img')
    namePromotion = models.CharField(max_length=50)

