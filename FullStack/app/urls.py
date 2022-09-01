from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('login_view/', login_view, name='login_view'),
    path('log_out_view/', log_out_view, name='log_out_view'),
    path('registration/', registration, name='registration'),
    path('profile/<str:pk>', profile, name='profile'),
    
    path('apartment/<int:pk>', apartment, name='apartment'),
    
    path('listing/', listing, name='listing'),
    path('agents/', agents, name='agents'),
    path('add_apartment/', add_apartment, name='add_apartment'),

]
