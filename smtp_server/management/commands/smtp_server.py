from django.core.management.base import BaseCommand, CommandError
import smtpd, asyncore, email
from emails.models import *


class Command(BaseCommand):
    help = 'Custom SMTP server daemon'

    def handle(self, *args, **options):
        server = CustomSMTPServer(('0.0.0.0', 25), None)
        asyncore.loop()


class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        #print 'Receiving message from:', peer
        #print 'Message addressed from:', mailfrom
        #print 'Message addressed to  :', rcpttos

        msg = email.message_from_string(data)
        body = ''
        if msg.get_content_maintype() == 'multipart':
            for part in msg.get_payload():
                if part.get_content_maintype() == 'text':
                    body = part.get_payload()
        else:
            body = msg.get_payload()

        _sender = User.objects.get_or_create(email=mailfrom)[0]
        for rcpt in rcpttos:
	        _receiver = User.objects.get_or_create(email=rcpt)[0]
	        Message(email=_receiver, sender=_sender, title=msg['Subject'], body=body, peer=peer).save()

        return

