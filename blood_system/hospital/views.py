from django.shortcuts import render

# Create your views here.
def hospitalhome(request):
    return render(request,'hospital_home.html')

def hospitallogin(request):
    return render(request,'hospital_login.html')

def hospitalsignup(request):
    return render(request,'hospital_registration.html')