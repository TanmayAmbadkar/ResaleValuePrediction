from django.db import models
from django.contrib.auth.models import User
from SellerUI.models import *
from BrokerUI.models import *
# Create your models here.

class VehiclesBought(models.Model):

    buyer = models.ForeignKey('BrokerUI.Profile', on_delete = models.CASCADE)
    vehicle = models.ForeignKey('SellerUI.Vehicle', on_delete = models.CASCADE)

    def __str_(self):
        return f"{self.buyer.username}: {self.vehicle.Vmodel}"
