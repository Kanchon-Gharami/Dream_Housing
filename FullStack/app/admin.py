from django.contrib import admin

from app.models import *
# Register your models here.

admin.site.register(MyCustomUser)
admin.site.register(Apartment)
admin.site.register(VisitRequest)
admin.site.register(BookingRequest)
admin.site.register(Notification)


