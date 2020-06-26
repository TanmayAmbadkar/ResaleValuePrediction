from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from BrokerUI.models import *
# Create your models here.

'''
class Profile(models.Model):

    user_types = (
        ('S', 'Seller'),
        ('C', 'Customer'),
        ('B', 'Broker'))
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    phone_number = models.CharField(max_length=10)
    type = models.CharField(max_length = 1, choices = user_types)

    def __str__(self):
        return self.user.username
'''

class Vehicle(models.Model):


    fueltanktypes = (
        ('P', 'PETROL'),
        ('D', 'DIESEL'),
        ('C', 'CNG'))
    seller = models.ForeignKey('BrokerUI.Profile', on_delete = models.CASCADE)
    Vmodel = models.CharField(max_length = 50)
    make = models.CharField(max_length = 20)
    desc = models.TextField()
    mileage = models.IntegerField()
    year = models.IntegerField()
    fueltank = models.CharField(max_length = 1, choices = fueltanktypes)
    price = models.IntegerField(blank = True)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    photo = models.ImageField(upload_to = 'vehicle_image', blank = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.Vmodel} {self.make}"

class VehiclePredPrice(models.Model):

    type_choices = [
        ("cng","cng"),
        ("petrol","petrol"),
        ("diesel","diesel"),
    ]
    make_choices = [
        ("renault","renault"),
        ("mahindra","mahindra"),
        ("maruti-suzuki","maruti-suzuki"),
        ("nissan","nissan"),
        ("bmw","bmw"),
        ("mercedes-benz","mercedes-benz"),
        ("hyundai","hyundai"),
        ("toyota","toyota"),
        ("audi","audi"),
        ("skoda","skoda"),
        ("ford","ford"),
        ("volkswagen","volkswagen"),
        ("tata","tata"),
        ("chevrolet","chevrolet"),
        ("cars-honda","cars-honda"),
    ]

    model_choices = [
        ("scala","scala"),
        ("benz-others","benz-others"),
        ("micra","micra"),
        ("x1","x1"),
        ("xuv300","xuv300"),
        ("sonata","sonata"),
        ("jetta","jetta"),
        ("suzuki-a-star","suzuki-a-star"),
        ("sumo","sumo"),
        ("honda-others","honda-others"),
        ("new-elantra","new-elantra"),
        ("suzuki-eeco","suzuki-eeco"),
        ("octavia","octavia"),
        ("fiesta","fiesta"),
        ("optra-magnum","optra-magnum"),
        ("benz-b-class","benz-b-class"),
        ("honda-crv","honda-crv"),
        ("benz-c-class","benz-c-class"),
        ("xylo","xylo"),
        ("vento","vento"),
        ("nano","nano"),
        ("lodgy","lodgy"),
        ("fabia","fabia"),
        ("fluidic-verna","fluidic-verna"),
        ("tuv","tuv"),
        ("accent","accent"),
        ("sonata-embera","sonata-embera"),
        ("scorpio","scorpio"),
        ("verito","verito"),
        ("tl","tl"),
        ("ikon","ikon"),
        ("free-style","free-style"),
        ("kwid","kwid"),
        ("honda-brio","honda-brio"),
        ("suzuki-ignis","suzuki-ignis"),
        ("suzuki-wagon-r","suzuki-wagon-r"),
        ("ameo","ameo"),
        ("tigor","tigor"),
        ("laura","laura"),
        ("honda-brv","honda-brv"),
        ("spark","spark"),
        ("ecosport","ecosport"),
        ("verna","verna"),
        ("elantra","elantra"),
        ("aria","aria"),
        ("a4","a4"),
        ("sail-uva","sail-uva"),
        ("i20","i20"),
        ("grand-i-10","grand-i-10"),
        ("3-series","3-series"),
        ("suzuki-swift","suzuki-swift"),
        ("fluence","fluence"),
        ("passat","passat"),
        ("7-series","7-series"),
        ("honda-city","honda-city"),
        ("suzuki-wagon-r-stingray","suzuki-wagon-r-stingray"),
        ("5-series","5-series"),
        ("honda-mobilio","honda-mobilio"),
        ("honda-city-zx","honda-city-zx"),
        ("suzuki-800","suzuki-800"),
        ("indica-v2","indica-v2"),
        ("suzuki-wagon-r-duo","suzuki-wagon-r-duo"),
        ("tiago","tiago"),
        ("escort","escort"),
        ("fusion","fusion"),
        ("etios-cross","etios-cross"),
        ("indigo-ecs","indigo-ecs"),
        ("superb","superb"),
        ("suzuki-vitara-brezza","suzuki-vitara-brezza"),
        ("suzuki-alto-k10","suzuki-alto-k10"),
        ("manza","manza"),
        ("terrano","terrano"),
        ("suzuki-gypsy","suzuki-gypsy"),
        ("nexon","nexon"),
        ("sonata-transform","sonata-transform"),
        ("getz","getz"),
        ("honda-civic","honda-civic"),
        ("indica-vista","indica-vista"),
        ("figo-aspire","figo-aspire"),
        ("a6","a6"),
        ("xuv500","xuv500"),
        ("suzuki-alto","suzuki-alto"),
        ("quanto","quanto"),
        ("micra-active","micra-active"),
        ("indica","indica"),
        ("safari-storme","safari-storme"),
        ("santro","santro"),
        ("grand-i10","grand-i10"),
        ("i10","i10"),
        ("xcent","xcent"),
        ("honda-jazz","honda-jazz"),
        ("getz-prime","getz-prime"),
        ("sail","sail"),
        ("vista","vista"),
        ("cross-polo","cross-polo"),
        ("fiesta-classic","fiesta-classic"),
        ("suzuki-ertiga","suzuki-ertiga"),
        ("endeavour","endeavour"),
        ("figo","figo"),
        ("hexa","hexa"),
        ("etios","etios"),
        ("polo","polo"),
        ("suzuki-others","suzuki-others"),
        ("bolt","bolt"),
        ("benz-e-class","benz-e-class"),
        ("suzuki-zen","suzuki-zen"),
        ("indigo-xl","indigo-xl"),
        ("honda-amaze","honda-amaze"),
        ("teana","teana"),
        ("eon","eon"),
        ("suzuki-stingray","suzuki-stingray"),
        ("suzuki-zen-estilo","suzuki-zen-estilo"),
        ("elite-i20","elite-i20"),
        ("safari","safari"),
        ("corolla-altis","corolla-altis"),
        ("optra","optra"),
        ("suzuki-estilo","suzuki-estilo"),
        ("indigo","indigo"),
        ("qualis","qualis"),
        ("tavera","tavera"),
        ("venture","venture"),
        ("cruze","cruze"),
        ("santro-xing","santro-xing"),
        ("aveo","aveo"),
        ("nuvosport","nuvosport"),
        ("fortuner","fortuner"),
        ("suzuki-celerio","suzuki-celerio"),
        ("corolla","corolla"),
        ("winger","winger"),
        ("zest-","zest-"),
        ("suzuki-esteem","suzuki-esteem"),
        ("kuv-100","kuv-100"),
        ("suzuki-alto-800","suzuki-alto-800"),
        ("enjoy","enjoy"),
        ("creta","creta"),
        ("honda-civic-hybrid","honda-civic-hybrid"),
        ("tiago-nrg","tiago-nrg"),
        ("santa-fe","santa-fe"),
        ("aspire","aspire"),
        ("bolero","bolero"),
        ("captiva","captiva"),
        ("etios-liva","etios-liva"),
        ("thar","thar"),
        ("koleos","koleos"),
        ("i20-active","i20-active"),
        ("suzuki-ciaz","suzuki-ciaz"),
        ("sunny","sunny"),
        ("yeti","yeti"),
        ("suzuki-sx4","suzuki-sx4"),
        ("duster","duster"),
        ("honda-wrv","honda-wrv"),
        ("rapid","rapid"),
        ("beat","beat"),
        ("suzuki-ritz","suzuki-ritz"),
        ("suzuki-baleno","suzuki-baleno"),
        ("honda-accord","honda-accord"),
        ("suzuki-versa","suzuki-versa"),
        ("camry","camry"),
        ("suzuki-wagon-r-1-0","suzuki-wagon-r-1-0"),
        ("suzuki-kizashi","suzuki-kizashi"),
        ("indigo-cs","indigo-cs"),
        ("innova","innova"),
        ("datsun-redi-go","datsun-redi-go"),
        ("suzuki-s-cross","suzuki-s-cross"),
        ("others","others"),
        ("aveo-u-va","aveo-u-va"),
        ("suzuki-swift-dzire","suzuki-swift-dzire"),
        ("pulse","pulse"),
        ("suzuki-omni","suzuki-omni"),
    ]

    Make = models.CharField(max_length = 50, choices = make_choices)
    Model = models.CharField(max_length = 50, choices = model_choices)
    Year = models.IntegerField()
    Type = models.CharField(max_length = 50, choices = type_choices)
    mileage = models.IntegerField()

    def __str__(self):
        return f"{self.make}: {self.model}"
