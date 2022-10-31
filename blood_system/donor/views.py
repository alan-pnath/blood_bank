from django.shortcuts import render
import mysql.connector as sql
un=''
ps=''
# Create your views here.
def loginaction(request):
    global un, ps
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="", database="blood")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                un = value
            if key == "pass":
                ps = value
        c = "select * from users where username='{}' and password='{}'".format(un, ps)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request, 'blood_login.html')
    return render(request, 'login_page.html')

def homeaction(request):
    return render(request,'home_page.html')


def signaction(request):

    global un,ps
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database="blood")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                un=value
            if key=="phone":
                ps=value
        c="insert into users(username,password)Values('{}','{}')".format(un,ps)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')