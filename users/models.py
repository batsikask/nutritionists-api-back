from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_nutritionist = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

class Address(models.Model):
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    street_number = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street}, {self.street_number}, {self.zip_code}, {self.city}, {self.country}"

class ContactInfo(models.Model):
    phone_type = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.phone_type}, {self.phone_number}"
    
    class Meta:
        verbose_name_plural = "Contact Info"

class NormalUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.ManyToManyField(Address, related_name='normal_users', blank=True)
    contact_info = models.ManyToManyField(ContactInfo, related_name='normal_users', blank=True)
    nutritionists = models.ManyToManyField('nutritionists.Nutritionist', related_name='client_nutritionists', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

