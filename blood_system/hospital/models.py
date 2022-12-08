from django.db import models
from phone_field import PhoneField

# Create your models here.
class Hospital_Users(models.Model):

    Hospital_Name = models.CharField(max_length=30)
    Address1 = models.CharField(max_length=1024)
    District = models.CharField(max_length=30)
    PinCode = models.CharField(max_length=8)
    PH_number = PhoneField(blank=True, help_text='Contact phone number')
    E_mail = models.EmailField(max_length=50)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Hospital_Name

class Blood_Stock(models.Model):
    Hospital_Name = models.CharField(max_length=30)
    Blood_Type=models.CharField(max_length=5)


    def __str__(self):
        return self.Hospital_Name