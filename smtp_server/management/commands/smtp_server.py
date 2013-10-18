from django.core.management.base import BaseCommand, CommandError
import smtpd, asyncore, email
from emails.models import *


class Command(BaseCommand):
    help = 'Custom SMTP server daemon'

    def handle(self, *args, **options):
        server = CustomSMTPServer(('0.0.0.0', 25), None)
        asyncore.loop()


def get_body_text(part, body_str = ''):
    if part.get_content_maintype() == 'text':
        return body_str + part.get_payload(decode=True) + '\n'
    if part.get_content_maintype() == 'multipart':
        for part in part.get_payload():
            body_str = get_body_text(part, body_str)
    return body_str

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        msg = email.message_from_string(data)
        body = get_body_text(msg)

        _sender = User.objects.get_or_create(email=mailfrom)[0]
        for rcpt in rcpttos:
            _receiver = User.objects.get_or_create(email=rcpt)[0]
            Message(email=_receiver, sender=_sender, title=msg['Subject'], body=body, peer=peer).save()

        return

