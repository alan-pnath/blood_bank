from django.shortcuts import render, get_object_or_404, redirect
from .models import Blood_Users
from .models import Blood_Donor_register
from django.http import HttpResponse
from hospital.models import Blood_Stock
from hospital.models import Hospital_Users
from django.db.models import Q



# Create your views here.
def medicio(request):
    return render(request, 'home_page.html')

def bloodsearch(request):
    results = []

    if request.method == "GET":

        query = request.GET.get('district') and request.GET.get('btype')
        if query == '':
            query = 'None'
            results = Blood_Stock.objects.filter(Q(Hospital_Name__icontains=query) | Q(District__icontains=query) | Q(Blood_Type__icontains=query))


        return render(request, 'bloodsearch.html',{'query': query, 'results': results})




    return render(request,'bloodsearch.html')


def donorreg(request):
    if request.method=="POST":

        First_Name = request.POST['first']
        last_Name = request.POST['last']
        age = request.POST['age']
        bloodtype = request.POST['type']
        dob = request.POST['dob']
        gender = request.POST['gender']
        add1 = request.POST['add1']
        add2 = request.POST['hospital']
        pin = request.POST['pin']
        district=request.POST['district']
        state = request.POST['state']
        weight = request.POST['weight']
        diabetic = request.POST['diab']
        hiv = request.POST['hiv']
        medicine = request.POST['medicine']
        medicinename = request.POST['medname']
        disease = request.POST['disease']
        diseasename = request.POST['Dname']
        surgery = request.POST['surg']
        surgeryname = request.POST['surgname']
        donated = request.POST['donateprev']
        donateddate = request.POST['dondate']


        ob=Blood_Donor_register()
        ob.First_Name=First_Name
        ob.Last_Name=last_Name
        ob.Age=age
        ob.Blood_Type=bloodtype
        ob.Date_Of_Birth=dob
        ob.Gender=gender
        ob.Address=add1
        ob.Hospital=add2
        ob.PinCode=pin
        ob.District=district
        ob.State=state
        ob.Weight=weight
        ob.Diabetic=diabetic
        ob.HIV=hiv
        ob.Medicine=medicine
        ob.Medicine_Name=medicinename
        ob.Disease=disease
        ob.Disease_Name=diseasename
        ob.Surgery=surgery
        ob.Surgery_Name=surgeryname
        ob.Donated_Previous=donated
        ob.Donated_Date=donateddate
        ob.status=0
        ob.save()
        return render(request, 'blood_login.html')

    value = Hospital_Users.objects.all()
    return render(request,'donor_register.html',{'register': value})



def loginaction(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = Blood_Users.objects.filter(E_mail=email, Password=password)
        if user:
            user_details = Blood_Users.objects.get(E_mail=email, Password=password)
            user_id = user_details.Full_Name
            request.session['id'] = user_id
            return render(request, 'blood_login.html',{'id':user_id})

        else:
            return HttpResponse('wrong user name or password or account does not exist!!')
    return render(request, 'login_page.html')


def bloodhome(request):
    return render(request,'blood_home.html')


def signaction(request):


    if request.method=="POST":
        Full_Name = request.POST['fullname']
        E_mail = request.POST['email']
        PH_number = request.POST['number']
        Password = request.POST['pass']

        ob=Blood_Users()
        ob.Full_Name = Full_Name
        ob.E_mail = E_mail
        ob.PH_number = PH_number
        ob.Password = Password
        if (Blood_Users.objects.filter(E_mail=E_mail)).exists():
            return HttpResponse('User name already exist!!')
        ob.status = 0
        ob.save()
        return render(request, 'login_page.html')
    return render(request, 'signup_page.html')


def logout(request):
    request.session.flush()
    return render(request, 'home_page.html')

