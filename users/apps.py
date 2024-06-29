from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from .signals import create_default_groups
        from django.db.models.signals import post_migrate
        post_migrate.connect(create_default_groups, sender=self)
