

from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=2)
        group, created = Group.objects.get_or_create(name='user_group')
        user.groups.add(group)
        user.save()
        group.save()