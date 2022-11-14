from django.db import models
from phone_field import PhoneField
# Create your models here.
class Organ_Users(models.Model):
    UserName = models.CharField(max_length=30)
    E_mail = models.EmailField(max_length=50)
    PH_number = PhoneField(blank=True, help_text='Contact phone number')
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.UserName