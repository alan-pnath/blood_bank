
from django.urls import path
from . views import *

urlpatterns = [

    path('hospitalhome/', hospitalhome, name="hosp_home"),
    path('hospitallogin/', hospitallogin, name="hosp_login"),
    path('hospitalsignup/', hospitalsignup, name="hosp_reg"),
    path('logout/', logout,name="logout"),
    path('blooddetails/',blooddetails,name="blood_details"),
    path('bloodinventory/', bloodinventory, name="blood_inv"),
    path('hospitalservice/', hospitalservice, name="hosp_serv"),
]