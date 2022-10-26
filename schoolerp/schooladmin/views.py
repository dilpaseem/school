from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'schooladmin/home.html')
def change_password(request):
    return render(request,'schooladmin/change_password.html')
def add_teachers(request):
    return render(request,'schooladmin/add_teachers.html')
def view_teachers(request):
    return render(request,'schooladmin/view_teachers.html')