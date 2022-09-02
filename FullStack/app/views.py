from multiprocessing import context
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import (
    make_password,
)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from app.decorators import *
from app.models import *

# Create your views here.

def index(request):
    context = {
        'latest_listing': Apartment.objects.filter(is_booked=False).order_by('-id')[:3:1],
        'rent_listing': Apartment.objects.filter(type='Rent').order_by('-id')[:5:1],
        'sale_listing': Apartment.objects.filter(
            Q(is_booked=False) & Q(type='Sale')
            ).order_by('-id')[:5:1],
        'agents': MyCustomUser.objects.filter(
            Q(is_agent=True) & Q(is_varified=True)
        ).order_by('-joined')[:5:1],
    }
    return render(request, "app/index.html", context)


def registration(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["confirm_password"]:
            try:
                with transaction.atomic():
                    u = MyCustomUser(
                        username=request.POST["username"],
                        password=make_password(request.POST["password"]),
                        email = request.POST['email'],
                        fullname = request.POST['fullname'], 
                        job = request.POST['job'], 
                        age = request.POST['age'], 
                        fb_link = request.POST['facebook'], 
                        twitter_link = request.POST['twitter'], 
                        linkedin_link = request.POST['linkedin'], 
                        website_link = request.POST['website'], 
                        about = request.POST['about'], 
                        img = request.FILES['img'], 
                    )
                    user_type = request.POST['user_type']
                    if user_type == 'Customer':
                        u.is_customer = True
                        u.is_varified = True
                    elif user_type == 'Agent':
                        u.is_customer = True
                    u.save()
                return redirect("app:index")
            except Exception as e:
                return render(request, "app/registration.html", {'errors': e})
        else:
            return render(request, "app/registration.html", {'errors': "Passwords do not match"})
    return render(request, "app/registration.html")


# logout view
def log_out_view(request):
    logout(request)
    return redirect("app:index")


# login view
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
    return redirect("app:index")


def profile(request, pk):
    this_user = MyCustomUser.objects.get(username=pk)
    visitor = MyCustomUser.objects.get(username=request.user.username)
    own_page = False
    allow_add = False
    if this_user == visitor:
        own_page = True
        if this_user.is_agent == True and this_user.is_varified == True:
            allow_add = True
    context={
        'this_user': this_user,
        'listing' : this_user.apartments.all(),
        'own_page': own_page,
        'allow_add': allow_add,
    }
    return render(request, "app/profile.html", context)


def listing(request):
    context = {
        'apartments' : Apartment.objects.filter(is_booked=False).order_by('-id'),
    }
    return render(request, "app/listing.html", context)


def rent_listing(request):
    context = {
        'apartments' : Apartment.objects.filter(type='Rent').order_by('-id'),
    }
    return render(request, "app/listing.html", context)


def sale_listing(request):
    context = {
        'apartments' : Apartment.objects.filter(
            Q(is_booked=False) & Q(type='Sale')
            ).order_by('-id')[:5:1],
    }
    return render(request, "app/listing.html", context)


def agents(request):
    context = {
        'agents': MyCustomUser.objects.filter(
            Q(is_agent=True) & Q(is_varified=True)
        ),
    }
    return render(request, "app/agents.html", context)


def apartment(request, pk):
    this_apartment = Apartment.objects.get(id=pk)
    agent = None
    own_apartment = False
    for i in this_apartment.user.all():
        if i.is_agent == True:
            agent = i
            break
    # check user is agent or not
    this_user = MyCustomUser.objects.get(username=request.user.username)
    if this_user == agent:
        own_apartment = True
    context = {
        'this_apartment' : this_apartment,
        'agent' : agent,
        'own_apartment' : own_apartment,
    }
    return render(request, "app/apartment.html", context)


def checkbox_val(request, x):
    if x in request.POST:
        return True
    else:
        return False


def add_apartment(request):
    this_user = MyCustomUser.objects.get(username=request.user.username)
    if request.method == "POST":
        if this_user.is_agent and this_user.is_varified:
            try:
                with transaction.atomic():
                    apartment_obj = Apartment(
                        name = request.POST['name'],
                        type = request.POST['type'],
                        location = request.POST['location'],
                        price = request.POST['price'],
                        area = request.POST['area'],
                        building_year = request.POST['building_year'],
                        img = request.FILES['img'],
                        about = request.POST['about'],
                        bedroom = request.POST['bedroom'],
                        living = request.POST['living'],
                        dinning = request.POST['dinning'],
                        bathroom = request.POST['bathroom'],
                        garage = checkbox_val(request, 'garage'),
                        watchman = checkbox_val(request, 'watchman'),
                        garden = checkbox_val(request, 'garden'),
                        swimmingpool = checkbox_val(request, 'swimmingpool'),
                        hospital = checkbox_val(request, 'hospital'),
                        shoppingmall = checkbox_val(request, 'shoppingmall'),
                    )
                    apartment_obj.save()
                    apartment_obj.user.add(this_user)
                    apartment_obj.save()
                    return redirect("app:profile", pk=this_user.pk)
            except Exception as e:
                return render(request, "app/add_apartment.html", {'errors': e})
    return render(request, "app/add_apartment.html")


