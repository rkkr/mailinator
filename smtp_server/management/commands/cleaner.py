from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from emails.models import *
from datetime import timedelta


class Command(BaseCommand):
    help = 'Database cleaner'

    def handle(self, *args, **options):
        #Delete emails
        Message.objects.filter(time_stamp__lt=timezone.now() - timedelta(1)).delete()

        #Delete users
        User.objects.filter(inbox__isnull=True, outbox__isnull=True).delete()

