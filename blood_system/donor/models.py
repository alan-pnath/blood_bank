from django.db import models
from phone_field import PhoneField



# Create your models here.

class Blood_Users(models.Model):
    Full_Name = models.CharField(max_length=30)
    E_mail = models.EmailField(max_length=50)
    PH_number = PhoneField(blank=True, help_text='Contact phone number')
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Full_Name


class Blood_Donor_register(models.Model):

    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age = models.PositiveIntegerField(null=False, blank=False)
    Blood_Type = models.CharField(max_length=3)
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(max_length=10)
    Address1 = models.CharField(max_length=1024)
    Address2 = models.CharField(max_length=1024)
    PinCode = models.CharField(max_length=8)
    District = models.CharField(max_length=30, null=True)
    State = models.CharField(max_length=15)
    Weight = models.FloatField(max_length=6)
    Diabetic = models.CharField(max_length=5)
    HIV = models.CharField(max_length=5)
    Medicine = models.CharField(max_length=5)
    Medicine_Name = models.CharField(max_length=30, null=True)
    Disease = models.CharField(max_length=5)
    Disease_Name = models.CharField(max_length=30, null=True)
    Surgery = models.CharField(max_length=5)
    Surgery_Name = models.CharField(max_length=30, null=True)
    Donated_Previous = models.CharField(max_length=5)
    Donated_Date = models.DateField(null=True)

    def __str__(self):
        return self.First_Name