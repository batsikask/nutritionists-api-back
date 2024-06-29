from django.contrib import admin
from .models import CustomUser, Address, ContactInfo, NormalUser

admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(ContactInfo)
admin.site.register(NormalUser)
