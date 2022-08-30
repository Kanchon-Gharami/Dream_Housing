from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('listing/', listing, name='listing'),
    path('profile/', profile, name='profile'),
    path('agents/', agents, name='agents'),

]
