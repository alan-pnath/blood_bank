from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render,redirect
from .models import *
from donor.models import Blood_Donor_register
from organ.models import Organ_Donor_Form

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
        return render(request, 'hospital_registration.html')
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
    userid = request.session['id']

    return render(request, 'hospital_services.html',{'id':userid})

def blooddetails(request):
    try:
        userid = request.session['id']
        data=Blood_Donor_register.objects.filter(Hospital=userid,status='pending')
        btyp=Blood_Donor_register.objects.get(Hospital=userid,status='pending')
        bt=btyp.Blood_Type
        request.session['b_type'] = bt
    except:
        return render(request, 'donor_table.html')

    return render(request, 'donor_table.html',{'register':data})

def accept(request):

    userid = request.session['id']
    breg = Blood_Donor_register.objects.get(Hospital=userid, status='pending')

    h_det=Hospital_Users.objects.get(Hospital_Name=userid)
    dis=h_det.District
    b_type = request.session['b_type']
    bs=Blood_Stock(Hospital_Name=userid,Blood_Type=b_type,District=dis)
    bs.save()
    breg.status='accepted'
    breg.save()


    return redirect('/')
def reject(request):

    userid = request.session['id']
    breg = Blood_Donor_register.objects.get(Hospital=userid, status='pending')
    breg.status='accepted'
    breg.save()


    return redirect('/hospitalservice')






def organtable(request):


    data = Organ_Donor_Form.objects.filter()
    return render(request,'organ_table.html',{'register':data})

