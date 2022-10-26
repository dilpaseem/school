from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'student/profile.html')
def change_password(request):
    return render(request,'student/change_password.html')    
    