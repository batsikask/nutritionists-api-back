# users/management/commands/check_superuser_group.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Check if the superuser is added to the Staff group.'

    def handle(self, *args, **options):
        username = 'admin'  # Replace with your superuser's username
        try:
            user = CustomUser.objects.get(username=username)
            staff_group = Group.objects.get(name='Staff')

            if staff_group in user.groups.all():
                self.stdout.write(self.style.SUCCESS(f"User {username} is a member of group 'Staff'."))
            else:
                self.stdout.write(self.style.ERROR(f"User {username} is not a member of group 'Staff'."))
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING(f"User {username} does not exist."))
        except Group.DoesNotExist:
            self.stdout.write(self.style.WARNING("Group 'Staff' does not exist."))

