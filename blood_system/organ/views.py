from django.shortcuts import render

# Create your views here.
def organsignup(request):
    return render(request,'organ_signup.html')

def organlogin(request):
    return render(request,'organ_login.html')
