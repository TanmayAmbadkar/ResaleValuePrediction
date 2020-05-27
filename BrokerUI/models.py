from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BrokerProfile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #additional

    phone_number = models.CharField(max_length = 10)

    #profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username

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
