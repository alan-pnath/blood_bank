from django.shortcuts import render
from .models import Organ_Users
from django.http import HttpResponse
from .models import *

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
        ob.Username = username
        ob.E_mail = E_mail
        ob.PH_number = PH_number
        ob.Password = Password
        if (Organ_Users.objects.filter(E_mail=E_mail)).exists():
            return HttpResponse('User name already exist!!')
        ob.status = 0
        ob.save()
        return render(request, 'organ_signup.html')
    return render(request,'organ_signup.html')

def organlogin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = Organ_Users.objects.filter(E_mail=email, Password=password)
        if user:
            user_details = Organ_Users.objects.get(E_mail=email, Password=password)
            user_id = user_details.Username
            request.session['id'] = user_id
            return render(request, 'organ_home2.html',{'id':user_id})
        else:
            return HttpResponse('wrong user name or password or account does not exist!!')
    return render(request,'organ_login.html')

def organform(request):


    if request.method == 'POST':
        first_Name = request.POST['first_name']
        middle_Name = request.POST['mid_name']
        last_Name = request.POST['last_name']
        fathersname = request.POST['fathers_name']
        mothersname = request.POST['mothers_name']
        address = request.POST['current_address']
        city = request.POST['city']
        district = request.POST['district']
        state = request.POST['state']
        pincode = request.POST['pincode']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        occupation = request.POST['occupation']
        blood_group = request.POST['blood_group']
        myfile = request.POST['myfile']
        emergency_contact_name = request.POST['emergency_contact_name']
        emergency_contact_phone = request.POST['emergency_contact_phone']
        emergency_contact_address = request.POST['emergency_contact_address']
        organ = request.POST['organ']

        ob = Organ_Donor_Form()
        ob.First_Name = first_Name
        ob.Middle_Name = middle_Name
        ob.Last_Name = last_Name
        ob.Father_Name = fathersname
        ob.Mother_Name = mothersname
        ob.Address = address
        ob.City = city
        ob.District = district
        ob.State = state
        ob.PinCode = pincode
        ob.Date_Of_Birth = birthday
        ob.Gender = gender
        ob.E_mail = email
        ob.PH_number = phone
        ob.Occupation = occupation
        ob.Blood_Group = blood_group
        ob.Id_Card = myfile
        ob.Emergency_Contact_Name = emergency_contact_name
        ob.Emergency_Contact_Phone = emergency_contact_phone
        ob.Emergency_Contact_Address = emergency_contact_address
        ob.Organ = organ
        ob.status = 0
        ob.save()
        return render(request, 'organ_home2.html')


    return render(request, 'organ_form.html')