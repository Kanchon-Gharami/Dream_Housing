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
    return render(request, "app/index.html")


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
                        img = request.POST['img'], 
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
    context={
        'this_user': this_user,
        'listing' : this_user.apartments.all()
    }
    return render(request, "app/profile.html", context)


def listing(request):
    apartments = Apartment.objects.order_by('id')
    context = {
        'apartments' : apartments
    }
    return render(request, "app/listing.html", context)


def agents(request):
    return render(request, "app/agents.html")


def apartment(request, pk):
    this_apartment = Apartment.objects.get(id=pk)
    agent = None
    for i in this_apartment.user.all():
        if i.is_agent == True:
            agent = i
            break
    context = {
        'this_apartment' : this_apartment,
        'agent' : agent,
    }
    return render(request, "app/apartment.html", context)


def on_off(x):
    if x == 'on':
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
                        img = request.POST['img'],
                        about = request.POST['about'],
                        bedroom = request.POST['bedroom'],
                        living = request.POST['living'],
                        dinning = request.POST['dinning'],
                        bathroom = request.POST['bathroom'],
                        garage = on_off(request.POST['garage']),
                        watchman = on_off(request.POST['watchman']),
                        garden = on_off(request.POST['garden']),
                        swimmingpool = on_off(request.POST['swimmingpool']),
                        hospital = on_off(request.POST['hospital']),
                        shoppingmall = on_off(request.POST['shoppingmall']),
                    )
                    apartment_obj.save()
                    apartment_obj.user.add(this_user)
                    apartment_obj.save()
                    return redirect("app:profile", pk=this_user.pk)
            except Exception as e:
                return render(request, "app/add_apartment.html", {'errors': e})
    return render(request, "app/add_apartment.html")


