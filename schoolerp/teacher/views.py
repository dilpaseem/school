from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'teacher/profile.html')
def change_password(request):
    return render(request,'teacher/change_password.html')
def add_student(request):
    return render(request,'teacher/add_student.html')
def view_student(request):
    return render(request,'teacher/view_student.html')      
