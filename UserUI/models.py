from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #additional

    phone_number = models.CharField(max_length = 15)

    #profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username
