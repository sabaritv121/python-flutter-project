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



class Review(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    feedback = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)



class Youtube_link(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    link = models.CharField(max_length=50)
    description = models.CharField(max_length=50)