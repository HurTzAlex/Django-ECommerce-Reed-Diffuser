from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse


# Create your views here.
# register อิมพอร์ท from django.contrib.auth.models import User
def register(request):
    
    # ถ้า เทธอด เท่ากับ โพสต์
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST['password']
        password_repeat = request.POST["password-repeat"]
        
        # ถ้า(1) username, email, password & password_repeat เป็นหรือเท่ากับค่าว่าง == ''
        if username == '' or email == '' or password == '' or password_repeat == '':
            messages.warning(request, 'กรุณาป้อนข้อมูลให้ครบ')
            return redirect('/register')

        # ถ้า(2) password & password_repeat ไม่เท่ากับ หรือ ไม่ตรงกัน
        if password != password_repeat:
            messages.warning(request, 'ใส่รหัสให้ตรงกันด้วยจ้า...')
            return redirect('/register')
        
        # ถ้า(3) username ทีในระบบแล้ว
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username นี้มีในระบบแล้ว กรุณาใช้ Username อื่น...')
            return redirect('/register')    
        
        # ถ้า(4) email มีในระบบแล้ว
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email นี้มีในระบบแล้ว กรุณาใช้ Email อื่น...')
            return redirect('/register')
        
        else:   
            # ถ้า(1-4) ใน form ไม่เป็นค่าว่าง, รหัสไม่ตรงกัน, username ไม่มีในระบบ และ email ไม่มีในระบบ
            # ให้ทำการสมัครสมาชิก
            user = User.objects.create_user(
                # username ตัวแปร = username ที่ส่งมาจาก form name
                username=username,
                email=email,
                password=password,
            )
            user.save()
            messages.success(request, 'สร้างบัญชีสำเร็จ')
            return redirect('/register')

        # ไว้เพิ่มหน้า login เมื่อสร้างบัญชีสำเร็จ

    else:
        return render(request, 'register.html')
        
        

# login อิมพอร์ท from django.contrib.auth.models import auth มาด้วย
def login(request):
    
    if request.method == "POST":
        # email เท่ากับ ค่า email ใน form (name="email")
        username = request.POST['username']
        password = request.POST['password']

        # ถ้า email หรือ password เท่ากับค่าว่าง
        if username == '' or password == '':
            messages.warning(request, 'กรุณาป้อนข้อมูลให้ครบ')
            return redirect('/login')
    
        else:
            # ส่ง email & password ไปตรวจสอบในฐานข้อมูล
            # auth.authenticate เป็นการตรวจสอบข้อมูลผู้ใช้ในฐานข้อมูล
            user = auth.authenticate(username=username, password=password)
            
            # ถ้า user ไม่เท่ากับ None 
            if user is not None:
                
            # ถ้ามีข้อมูลผู้ใช้ในฐานข้อมูล จะให้ล้อคอินเข้าสู่ระบบได้
            # login ต้องส่ง request, user 
                auth.login(request, user)
                
                # redirect ไปยังหน้าแรก(หน้าหลัก)
                return redirect('/')
                
            # ถ้าไม่มีข้อมูลผู้ใช้งาน จะทำการส่งข้อความเตือน
            else:
                messages.warning(request, 'ไม่พบข้อมูลบัญชีผู้ใช้งาน')
                return redirect('/login')
                
            
    else:
        return render(request, 'login.html')


def logout(request):
    
    # นำข้อมูล User มาทำการ Logout
    auth.logout(request)
    
    return redirect(reverse('login'))