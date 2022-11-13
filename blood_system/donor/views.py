from django.shortcuts import render
from .models import Blood_Users
# from django.contrib.auth.models import User,auth
import mysql.connector as sql
from django.http import HttpResponse


un=''
ps=''
# Create your views here.
def medicio(request):
    return render(request, 'home_page.html')


def donorreg(request):
    global  fn,ln, ag, ty, db, gen, ad1, ad2, pin, st, wg, diab, hv, med, Mname, ds, Dname, surg, Sname, donprev, dondate
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="", database="medicio")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first":
                fn = value
            if key == "last":
                ln = value
            if key == "age":
                ag = value
            if key == "type":
                ty = value
            if key == "dob":
                db = value
            if key == "gender":
                gen = value
            if key == "add1":
                ad1 = value
            if key == "add2":
                ad2 = value
            if key == "pin":
                pin = value
            if key == "state":
                st = value
            if key == "weight":
                wg = value
            if key == "diab":
                diab = value
            if key == "hiv":
                hv = value
            if key == "medicine":
                med = value
            if key == "medname":
                Mname = value
            if key == "disease":
                ds = value
            if key == "Dname":
                Dname= value
            if key == "surg":
                surg = value
            if key == "surgname":
                Sname = value
            if key == "donateprev":
                donprev = value
            if key == "dondate":
                dondate = value

        c = "insert into blood_donor_reg(First_Name,Last_Name,Age,Blood_Type,DOB,Gender,Address1,Address2,Pincode,State,Weight,Diabetic,HIV,Medicine,Medicine_Name,Disease,Disease_Name,Surgery,Surgery_Name,Donated_Prev,Donated_Date)Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})".format(fn,ln, ag, ty, db, gen, ad1, ad2, pin, st, wg, diab, hv, med, Mname, ds, Dname, surg, Sname, donprev, dondate)
        cursor.execute(c)
        m.commit()
        return render(request, 'blood_home.html')
    return render(request,'donor_register.html')



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
    else:
        return render(request, 'signup_page.html')


    return render(request,'signup_page.html')