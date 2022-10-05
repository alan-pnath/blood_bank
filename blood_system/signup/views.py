from django.shortcuts import render
import mysql.connector as sql
un=''
ps=''

# Create your views here.
def homeaction(request):
    return render(request,'home_page.html')


def signaction(request):
    global un,ps
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database="blood")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                un=value
            if key=="psw":
                ps=value
        c="insert into users Values('{}','{}')".format(un,ps)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')