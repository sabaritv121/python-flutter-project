from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class Login(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_workshop=models.BooleanField(default=False)
    address=models.CharField(max_length=40)
    phone_number=models.CharField(max_length=20)
    workshop_name=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    location=models.CharField(max_length=40)
    min_wage =models.CharField(max_length=50)

#test
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField()
#test
class mark(models.Model):
    user=models.ForeignKey(Student,on_delete=models.CASCADE, null=True)
    roll_no=models.CharField(max_length=100)





#workrequest


class Workrequest(models.Model):
    customer = models.ForeignKey(Login, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='workshop')
    name = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=20)
    problem=models.CharField(max_length=20)
    location = models.CharField(max_length=40)
    date=models.DateField()
    time=models.TimeField()
    phone_number=models.CharField(max_length=20)
    status=models.CharField(max_length=20)