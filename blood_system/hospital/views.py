from django.http import HttpResponse
from django.shortcuts import render
from .models import Hospital_Users


# Create your views here.
def hospitalhome(request):
    return render(request, 'hospital_home.html')


def hospitallogin(request):
    return render(request, 'hospital_login.html')


def hospitalsignup(request):
    if request.method == "POST":
        HospName = request.POST['hospname']
        address = request.POST['address']
        district = request.POST['district']
        pincode = request.POST['pin']
        PH_number = request.POST['number']
        E_mail = request.POST['email']
        Password = request.POST['password']

        ob = Hospital_Users()
        ob.Full_Name = HospName
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
