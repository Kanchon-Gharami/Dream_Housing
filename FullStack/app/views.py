from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "app/index.html")


def listing(request):
    return render(request, "app/listing.html")


def profile(request):
    return render(request, "app/profile.html")


def agents(request):
    return render(request, "app/agents.html")


def apartment(request):
    return render(request, "app/apartment.html")


def registration(request):
    return render(request, "app/registration.html")


def add_apartment(request):
    return render(request, "app/add_apartment.html")
