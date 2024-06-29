from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group
from django.apps import apps

def create_default_groups(sender, **kwargs):
    groups = ['Staff', 'NormalUser', 'Nutritionist'] 
    for group in groups:
        Group.objects.get_or_create(name=group)