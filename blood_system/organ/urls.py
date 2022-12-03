
from django.urls import path
from . views import *

urlpatterns = [

path('organsignup/',organsignup,name="organ_signup"),
    path('organlogin/',organlogin,name="organ_login"),
    path('organhome/',organhome,name="organ_home"),
]