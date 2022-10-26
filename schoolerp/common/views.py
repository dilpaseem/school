from django.shortcuts import render,redirect

from common.models import AdminLogin

# Create your views here.

def admin_login(request):
    if request.method == 'POST' :
        print('*****')
        user_name = request. POST ['admin_login']
        password = request. POST ['password']
        try :
            ad_login = AdminLogin.objects.get(username = user_name,password = password)
            return redirect('school_admin:home')
        except :
            return render(request,'common/admin_login.html')

         
    return render(request,'common/admin_login.html')
def product_home(request):
    return render(request,'common/product_home.html')
def student_login(request):
    return render(request,'common/student_login.html')
def teacher_login(request):
    return render(request,'common/teacher_login.html')
