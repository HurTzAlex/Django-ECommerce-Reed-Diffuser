from django.contrib import admin
from products_app.models import Product, ProductPromotion

# จัดการหน้า /admin ให้สามารถอ่านค่าได้ง่าย เดิมจะเป็น Product Object(1)
class ManageProduct(admin.ModelAdmin):
    
    # นำโมเดล Product มากำหนดว่าจะให้อ่านค่าอะไรบ้าง ในหน้า /admin
    list_display = [
        'name',
        'price',
        'stock',
        'isTrending',
    ]
    
    # เราสามารถเปลี่ยนแปลงค่าตามด้านล่าง โดยที่ไม่ต้องเข้าไปแก้ไขทีละไฟล์ ในหน้า /admin
    list_editable = [
        'price',
        'stock',
        'isTrending',
    ]
    
    # กำหนดให้แสดงสินค้า ต่อหน้า กี่รายการ เดิมจะแสดงทั้งหมด ต่อ 1 หน้า
    # list_per_page = 4
    
    # ระบบค้นหาข้อมูล โดยใช้ ชื่อ ในหน้า /admin
    search_fields = [
        'name'
    ]

    # ตัวกรองในการเช็คสินค้า ขายดี หรือเป็นทีี่นิยมหรือไม่ ในหน้า /admin โดยใช้ isFrending
    list_filter = [
        'isTrending'
    ]
    

class ManageProductPromotion(admin.ModelAdmin):
    list_display = [
        'namePromotion',
        'imagePromotion',
    ]
    
    

# กำหนดให้ Admin สามารถเพิ่ม ลบ สินค้าได้ ของ class Product() ใน models.py(products_app)
# อย่าลืมนำ ManageProduct มาอ้างอิง
admin.site.register(Product, ManageProduct)
admin.site.register(ProductPromotion, ManageProductPromotion)