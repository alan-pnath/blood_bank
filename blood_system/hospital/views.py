from django.shortcuts import render

# Create your views here.
def hospitalhome(request):
    return render(request,'hospital_home.html')