
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        admin = User.objects.create_superuser(email="andre.catarino.guerra@protonmail.com", username="guerra", password="guerra")
        admin.save()
        