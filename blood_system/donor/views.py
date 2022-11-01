from django.shortcuts import render
import mysql.connector as sql
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
    global un, ps
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="", database="medicio")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                un = value
            if key == "pass":
                ps = value
        c = "select * from blood_user where E_mail='{}' and Password='{}'".format(un, ps)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request, 'blood_login.html')
    return render(request, 'login_page.html')

def bloodhome(request):
    return render(request,'blood_home.html')


def signaction(request):

    global un,ps,fn,pn
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database="medicio")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "fullname":
                fn = value
            if key=="email":
                un=value
            if key=="number":
                pn=value
            if key=="pass":
                ps=value
        c="insert into blood_user(Full_Name,E_mail,Ph_number,Password)Values('{}','{}','{}','{}')".format(fn,un,pn,ps)
        cursor.execute(c)
        m.commit()
        return render(request, 'login_page.html')
    return render(request,'signup_page.html')