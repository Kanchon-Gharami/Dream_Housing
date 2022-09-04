from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('login_view/', login_view, name='login_view'),
    path('log_out_view/', log_out_view, name='log_out_view'),
    path('registration/', registration, name='registration'),
    path('profile/<str:pk>', profile, name='profile'),
    path('delete_profile/<str:pk>', delete_profile, name='delete_profile'),
    path('notification', notification, name='notification'),
    
    path('listing/', listing, name='listing'),
    path('rent_listing/', rent_listing, name='rent_listing'),
    path('sale_listing/', sale_listing, name='sale_listing'),
    path('search_result/', search_result, name='search_result'),
    
    path('apartment/<int:pk>', apartment, name='apartment'),
    path('add_apartment/', add_apartment, name='add_apartment'),
    path('edit_apartment/<int:pk>', edit_apartment, name='edit_apartment'),
    path('delete_apartment/', delete_apartment, name='delete_apartment'),
    path('agents/', agents, name='agents'),
    
    path('pay_a_visit/', pay_a_visit, name='pay_a_visit'),
    path('booking/', booking, name='booking'),

]

