from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('listing/', listing, name='listing'),
    path('profile/', profile, name='profile'),
    path('agents/', agents, name='agents'),
    path('apartment/', apartment, name='apartment'),
    path('add_apartment/', add_apartment, name='add_apartment'),
    path('registration/', registration, name='registration'),

]
