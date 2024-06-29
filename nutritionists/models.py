from django.db import models
from users.models import CustomUser, Address, ContactInfo, NormalUser

class Education(models.Model):
    education_level = models.CharField(max_length=30, null=True, blank=True)
    education_title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.education_level}, {self.education_title}"
    
    class Meta:
        verbose_name_plural = "Education"

class Nutritionist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    personal_address = models.ManyToManyField(Address, related_name="nutritionist_personal_addresses", blank=True)
    office_address = models.ManyToManyField(Address, related_name="nutritionists_office_addresses", blank=True)
    contact_info = models.ManyToManyField(ContactInfo, related_name="nutritionist_contact_info", blank=True)
    education = models.ManyToManyField(Education, related_name="nutritionist_education", blank=True)
    is_active = models.BooleanField(default=True)
    clients = models.ManyToManyField(NormalUser, related_name="nutritionist_clients", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
