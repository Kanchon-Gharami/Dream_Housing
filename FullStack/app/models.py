from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.
class MyCustomUser(AbstractUser):
    username = models.CharField(
        max_length=100, unique="True", blank=False, primary_key=True
    )
    password = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    job = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    fb_link = models.URLField(max_length=200, blank=True, null=True)
    twitter_link = models.URLField(max_length=200, blank=True, null=True)
    linkedin_link = models.URLField(max_length=200, blank=True, null=True)
    website_link = models.URLField(max_length=200, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    joined = models.DateField(default=datetime.now)
    img = models.ImageField(upload_to ='images/')

    is_agent = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_varified = models.BooleanField(default=False)

    def __str__(self):
        return self.username



class Apartment(models.Model):
    type=[
        ( 'Rent','Rent'),
        ( 'Sale','Sale'),
    ]
    user = models.ManyToManyField(MyCustomUser, related_name='apartments')
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=20, choices=type, default='Rent')
    location =  models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField()
    area = models.IntegerField()
    building_year = models.DateField()
    img = models.ImageField(upload_to ='apartment/')
    about = models.TextField()
    # Features
    bedroom = models.IntegerField()
    living = models.IntegerField()
    dinning = models.IntegerField()
    bathroom = models.IntegerField()
    # Facilities
    garage = models.BooleanField(default=False)
    watchman = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    swimmingpool = models.BooleanField(default=False)
    hospital = models.BooleanField(default=False)
    shoppingmall = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
