# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(userDetails)
admin.site.register(membershipDetails)
admin.site.register(registrationDetails)
admin.site.register(eventDetails)
