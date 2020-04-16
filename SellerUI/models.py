from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SellerProfile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #additional

    phone_number = models.CharField(max_length = 15)

    #profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username

class Vehicle(models.Model):


    fueltanktypes = (
        ('P', 'PETROL'),
        ('D', 'DIESEL'),
        ('C', 'CNG'))
    Vmodel = models.CharField(max_length = 50)
    make = models.CharField(max_length = 20)
    desc = models.TextField()
    age = models.IntegerField()
    mileage = models.IntegerField()
    year = models.IntegerField()
    fueltank = models.CharField(max_length = 1, choices = fueltanktypes)
    price = models.IntegerField(blank = True)

    def __str__(self):
        return

class VehicleListed(models.Model):

    vehicleID = models.ForeignKey(Vehicle, on_delete= models.CASCADE)
    sellerID = models.ForeignKey(SellerProfile, on_delete= models.CASCADE)
