from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SellerProfile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #additional

    phone_number = models.IntegerField(max_length=10)

    def __str__(self):
        return self.user.username

class Vehicle(models.Model):


    fueltanktypes = (
        ('P', 'PETROL'),
        ('D', 'DIESEL'),
        ('C', 'CNG'))
    seller = models.ForeignKey('SellerProfile', on_delete = models.CASCADE)
    Vmodel = models.CharField(max_length = 50)
    make = models.CharField(max_length = 20)
    desc = models.TextField()
    age = models.IntegerField()
    mileage = models.IntegerField()
    year = models.IntegerField()
    fueltank = models.CharField(max_length = 1, choices = fueltanktypes)
    price = models.IntegerField(blank = True)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.Vmodel} {self.make}"

class VehiclePred(models.Model):
    vehicleID= models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    predprice = models.IntegerField()
    actualprice = models.IntegerField()

    def __str__(self):
        return predprice
