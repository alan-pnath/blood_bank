
from django.urls import path
from . views import *

urlpatterns = [

path('hospitalhome/', hospitalhome, name="hosp_home"),
    path('hospitallogin/', hospitallogin, name="hosp_login"),
    path('hospitalsignup/', hospitalsignup, name="hosp_reg"),
]