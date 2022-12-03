from django.shortcuts import render
from .models import Organ_Users
from django.http import HttpResponse

# Create your views here.
def organhome(request):
    return render(request,'organ_home.html')

def organsignup(request):


    if request.method == "POST":
        username = request.POST['username']
        E_mail = request.POST['email']
        PH_number = request.POST['phone']
        Password = request.POST['password']

        ob=Organ_Users()
        ob.Full_Name = username
        ob.E_mail = E_mail
        ob.PH_number = PH_number
        ob.Password = Password
        if (Organ_Users.objects.filter(E_mail=E_mail)).exists():
            return HttpResponse('User name already exist!!')
        ob.status = 0
        ob.save()
        return render(request, 'organ_login.html')
    return render(request,'organ_signup.html')

def organlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = Organ_Users.objects.filter(E_mail=email, Password=password)
        if user:
            user_details = Organ_Users.objects.get(E_mail=email, Password=password)
            user_id = user_details.Full_Name
            request.session['id'] = user_id
            return render(request,'home_page.html',{'id':user_id})

        else:
            return HttpResponse('wrong user name or password or account does not exist!!')
    return render(request,'organ_login.html')
