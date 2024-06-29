# Generated by Django 5.0.6 on 2024-06-29 22:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nutritionists', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionist',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='nutritionist_clients', to='users.normaluser'),
        ),
        migrations.AddField(
            model_name='nutritionist',
            name='contact_info',
            field=models.ManyToManyField(blank=True, related_name='nutritionist_contact_info', to='users.contactinfo'),
        ),
        migrations.AddField(
            model_name='nutritionist',
            name='education',
            field=models.ManyToManyField(blank=True, related_name='nutritionist_education', to='nutritionists.education'),
        ),
        migrations.AddField(
            model_name='nutritionist',
            name='office_address',
            field=models.ManyToManyField(blank=True, related_name='nutritionists_office_addresses', to='users.address'),
        ),
        migrations.AddField(
            model_name='nutritionist',
            name='personal_address',
            field=models.ManyToManyField(blank=True, related_name='nutritionist_personal_addresses', to='users.address'),
        ),
        migrations.AddField(
            model_name='nutritionist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]