from django.http import HttpResponse
from django.shortcuts import render
from .models import Hospital_Users


# Create your views here.
def hospitalhome(request):
    return render(request, 'hospital_home.html')


def hospitallogin(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('password')
        user = Hospital_Users.objects.filter(E_mail=email, Password=password)
        if user:
            user_details = Hospital_Users.objects.get(E_mail=email, Password=password)
            user_id = user_details.Hospital_Name
            request.session['id'] = user_id
            return render(request, 'hospital_services.html',{'id':user_id})
        else:
            return HttpResponse('wrong user name or password or account does not exist!!')
    return render(request,'hospital_login.html')


def hospitalsignup(request):
    if request.method == "POST":
        HospName = request.POST['hospname']
        address = request.POST['address']
        district = request.POST['district']
        pincode = request.POST['pin']
        PH_number = request.POST['phone']
        E_mail = request.POST['email']
        Password = request.POST['password']

        ob = Hospital_Users()
        ob.Hospital_Name = HospName
        ob.Address1 = address
        ob.District = district
        ob.PinCode = pincode
        ob.PH_number = PH_number
        ob.E_mail = E_mail
        ob.Password = Password
        if (Hospital_Users.objects.filter(E_mail=E_mail)).exists():
            return HttpResponse('User name already exist!!')
        ob.status = 0
        ob.save()
        return render(request, 'hospital_login.html')
    else:
        return render(request, 'hospital_registration.html')

    return render(request, 'hospital_registration.html')

def logout(request):
    request.session.flush()
    return render(request, 'home_page.html')