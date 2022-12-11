from django.db import models

# Create your models here.
class Organ_Users(models.Model):
    Username = models.CharField(max_length=30)
    E_mail = models.CharField(max_length=50)
    PH_number = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Username