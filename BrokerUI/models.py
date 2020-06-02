from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class RealEstate(models.Model):
#
#     house_type = (('A', ''))
#     lat = models.FloatField()
#     lon = models.FloatField()
#     builtuparea = models.IntegerField()
#     carpetarea = models.IntegerField()
#     area = models.CharField()
#     address = models.TextField()
    #type = model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    choices = [('U','User'),('S','Seller'),('B','Broker')]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=1,choices=choices,default='none')
    phone_number = models.CharField(max_length=5)
    is_user= models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name

class Estate(models.Model):
    broker = models.ForeignKey(Profile,on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    price = models.FloatField()
    bedroom = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    carpetarea = models.IntegerField()
    builtuparea = models.IntegerField()
    def __str__(self):
        return self.broker.user.first_name

    def get_absolute_url(self):
        return reverse('estate_detail',kwargs={'pk':self.pk})
