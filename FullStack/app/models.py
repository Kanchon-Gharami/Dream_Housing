from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

'''

class MyCustomUser(AbstractUser):
    username = models.CharField(
        max_length=100, unique="True", blank=False, primary_key=True
    )
    password = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    fullname = models.CharField(max_length=200, blank=False, null=False)
    job = models.CharField(max_length=200, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    fb_link = models.URLField(max_length=200, blank=False, null=False)
    twitter_link = models.URLField(max_length=200, blank=False, null=False)
    linkedin_link = models.URLField(max_length=200, blank=False, null=False)
    website_link = models.URLField(max_length=200, blank=False, null=False)
    about = models.TextField(blank=False, null=False)
    img = models.ImageField(upload_to ='media')

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
    agent = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    type = models.CharField(max_length=20, choices=type, default='Rent')
    location =  models.CharField(max_length=200, blank=False, null=False)
    price = models.IntegerField()
    area = models.IntegerField()
    building_year = models.DateField()
    img = models.ImageField(upload_to ='media')
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

    def __str__(self):
        return self.name
    
'''