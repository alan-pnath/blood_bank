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

