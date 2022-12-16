from django.db import models

# Create your models here.
class Organ_Users(models.Model):
    Username = models.CharField(max_length=30)
    E_mail = models.CharField(max_length=50)
    PH_number = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Username

class Organ_Donor_Form(models.Model):

    User_Id = models.ForeignKey(Organ_Users, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Middle_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Father_Name = models.CharField(max_length=30)
    Mother_Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=1024)
    City = models.CharField(max_length=30)
    District = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    PinCode = models.CharField(max_length=8)
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(max_length=10)
    E_mail = models.CharField(max_length=50)
    PH_number = models.CharField(max_length=15)
    Occupation = models.CharField(max_length=20)
    Blood_Group = models.CharField(max_length=5)
    Id_Card = models.FileField(upload_to='documents/')
    Emergency_Contact_Name = models.CharField(max_length=30)
    Emergency_Contact_Phone = models.CharField(max_length=15)
    Emergency_Contact_Address = models.CharField(max_length=30)
    Organ = models.CharField(max_length=10)

    def __str__(self):
        return self.First_Name