from django.contrib import admin

from cart_app.models import Cart

# กำหนดให้ admin สามารถจัดการคลาส Cart (อย่าลืม import models Cart) + CartItem
admin.site.register(Cart)