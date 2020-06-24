from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):

    user_types = (
        ('S', 'Seller'),
        ('C', 'Customer'),
        ('B', 'Broker'))
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=10)
    type = models.CharField(max_length = 1, choices = user_types)


    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse('broker_detail', kwargs={'pk':self.pk})

class Estate(models.Model):
    broker = models.ForeignKey(Profile, on_delete=models.CASCADE)
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


class Prediction(models.Model):
    spell_choices = [('DISCERN_LOCATION','DISCERN_LOCATION'),('GEAS','GEAS')]
    sublocality_choices= [
        ('Gotri','Gotri'),
        ('Vasna','Vasna'),
        ('Atladara','Atladara'),
        ('Manjalpur','Manjalpur'),('Akota','Akota'),
        ('Karelibaugh','Karelibaugh'),
        ('Danteshwar','Danteshwar'),
        ('Sun Pharma Padra Road','Sun Pharma Padra Road'),
        ('Dabhoi Road','Dabhoi Road'),('Samta','Samta'),
        ('Wadi','Wadi'),('Bhayli','Bhayli'),
        ('Kalali','Kalali'),
        ('Vadsar','Vadsar'),
        ('akshar chowk','akshar chowk')
    ]
    type_choices = [
        ('apartments','apartments'),
        ('sale-floors','sale-floors'),
        ('houses','houses')
    ]
    rooms_choices = [
         (1,1),
         (2,2),
         (3,3)
     ]
    bathrooms_choies = [
        (1,1),
        (2,2),
        (3,3)
    ]
    furnished_choices = [
        ('no','no'),
        ('yes','yes'),
        ('semi','semi')
     ]
    constructionstatus_choices=[
        ('under_construction','under_construction'),
        ('launched','launched'),
        ('ready_to_move','ready_to_move')
    ]
    project_choices=[
        ('Pavilion Heights: PR/GJ/VADODARA/VADODARA/Others/RAA05921/210819','Pavilion Heights'),
        ('Devesh Imperia','Devesh Imperia'),
        ('White lotus','White lotus'),
        ('PRAKRUTI','PRAKRUTI'),
        ('STATUS','STATUS'),
        ('Ananta swagatam','Ananta swagatam'),
        ('Saakar belleza','Saakar belleza'),
        ('SAMRUDDHI','SAMRUDDHI'),
        ('VIHAV SKYONE: PR/GJ/VADODARA/VADODARA/Others/MAA03997/061118','VIHAV SKYONE'),
        ('Gotbull','Gotbull'),
        ('PARAM BLISS','PARAM BLISS'),
        ('Anant park society','Anant park society'),
        ('NAMAN HEIGHTS','NAMAN HEIGHTS'),
        ('PARAM CREST','PARAM CREST'),
        ('Dwarkesh Avenue','Dwarkesh Avenue'),
        ('Girikunj Apartment','Girikunj Apartment'),
        ('GOLDEN VALLEY','GOLDEN VALLEY'),
        ('GUNATIT RESIDENCY','GUNATIT RESIDENCY'),
        ('SHYAMAL COUNTY- TYPE-B','SHYAMAL COUNTY'),
        ('PARAM CREST-PR/GJ/VADODARA/VADODARA/Others/MAA05269/120419','PARAM CREST')
    ]

    spell = models.CharField(max_length = 30, choices = spell_choices)
    sublocality_level = models.CharField(max_length = 100, choices = sublocality_choices)
    lat = models.FloatField()
    long = models.FloatField()
    type = models.CharField(max_length = 15, choices = type_choices)
    rooms = models.IntegerField(choices = rooms_choices)
    bathrooms = models.IntegerField(choices = bathrooms_choies)
    furnished = models.CharField(max_length = 5, choices = furnished_choices)
    constructionstatus = models.CharField(max_length = 50, choices = constructionstatus_choices)
    ft = models.FloatField()
    carpetarea = models.FloatField()
    project = models.CharField(max_length = 150, choices = project_choices)

    def _str__(self):
        return f'{self.project} {self.rooms}'
