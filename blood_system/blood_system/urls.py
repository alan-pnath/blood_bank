"""blood_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from donor import views
from organ.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',views.medicio,name="medicio"),
    path('bloodhome/', views.bloodhome,name="blood_home"),
    path('admin/', admin.site.urls),
    path('loginaction/', views.loginaction,name="login"),
    path('signupaction/', views.signaction,name="signup"),
    path('organsignup/',organsignup,name="organ_signup"),
    path('organlogin/',organlogin,name="organ_login"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
