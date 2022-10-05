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
            if key == "uname":
                un = value
            if key == "psw":
                ps = value
        c = "select * from users where username='{}' and password='{}'".format(un, ps)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request, 'welcome.html')
    return render(request, 'login_page.html')