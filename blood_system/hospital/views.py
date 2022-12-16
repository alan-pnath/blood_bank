from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from donor.models import Blood_Donor_register


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


def bloodinventory(request):

    num1 = Blood_Stock.objects.filter(Blood_Type='A+').count()
    num2 = Blood_Stock.objects.filter(Blood_Type='A-').count()
    num3 = Blood_Stock.objects.filter(Blood_Type='B+').count()
    num4 = Blood_Stock.objects.filter(Blood_Type='B-').count()
    num5 = Blood_Stock.objects.filter(Blood_Type='AB+').count()
    num6 = Blood_Stock.objects.filter(Blood_Type='AB-').count()
    num7 = Blood_Stock.objects.filter(Blood_Type='O+').count()
    num8 = Blood_Stock.objects.filter(Blood_Type='O-').count()

    return render(request, 'blood_inventory.html',{'Ap':num1,'An':num2,'Bp':num3,'Bn':num4,'ABp':num5,'ABn':num6,'Op':num7,'On':num8})

def hospitalservice(request):

    return render(request, 'hospital_services.html')

def blooddetails(request):
    # if request.method == "POST":
    #     statusAccept = request.POST.get("action") == "accept"
    #     statusReject = request.POST.get("action") == "reject"
    #     if statusAccept:
    #         try:
    #
    #             bloodtype = request.POST['{{x.Blood_Type}}']
    #             ob = Blood_Stock()
    #             ob.Blood_Type= bloodtype
    #             ob.status = 0
    #             ob.save()
    #             return render(request, 'donor_table.html')
    #
    #         except Exception as e:
    #             return HttpResponse("failed{}".format(e))
    #
    #     # if statusReject:
    #     #     remove = Blood_Donor_register.objects.get(First_Name=First_Name)
    #     #     remove.delete()

    data=Blood_Donor_register.objects.filter()
    return render(request, 'donor_table.html',{'register':data})

