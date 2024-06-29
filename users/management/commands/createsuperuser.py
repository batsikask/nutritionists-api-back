from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser, and add them to the staff group.'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        username = options.get('username')
        if username:
            user = get_user_model().objects.get(username=username)
        else:
            user = get_user_model().objects.latest('id')
        staff_group, created = Group.objects.get_or_create(name='Staff')
        user.groups.add(staff_group)
        self.stdout.write(self.style.SUCCESS(f"{user.username} added to group 'Staff'."))
