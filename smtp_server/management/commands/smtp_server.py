from django.core.management.base import BaseCommand, CommandError
from django.db import connection
import smtpd, asyncore, email, platform, time, datetime, sys, traceback
from emails.models import *


class Command(BaseCommand):
    help = 'Custom SMTP server daemon'

    def handle(self, *args, **options):
        while True:
            try:
                log('Starting smtp server')
                server = CustomSMTPServer(('0.0.0.0', 25), None)
                asyncore.loop()
            except:
                log_exception()
                time.sleep(1)


def get_body_text(part, body_str = ''):
    if part.get_content_maintype() == 'text':
        return body_str + part.get_payload(decode=True) + '\n'
    if part.get_content_maintype() == 'multipart':
        for part in part.get_payload():
            body_str = get_body_text(part, body_str)
    return body_str

def log_exception():
    log('Exception')
    traceback.print_exc(file=open('/var/log/pysmtpd', 'a'))

def log(message):
    with open('/var/log/pysmtpd', 'a') as file:
        file.write(str(datetime.datetime.now()) + ' : ' + message + '\n')


class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        try:
            msg = email.message_from_string(data)
            body = get_body_text(msg)

            for rcpt in rcpttos:
                if rcpt.split('@')[1].split('.')[0].lower() <> platform.node().lower():
                    continue
                _sender = User.objects.get_or_create(email=mailfrom)[0]
                _receiver = User.objects.get_or_create(email=rcpt)[0]
                Message(email=_receiver, sender=_sender, title=msg['Subject'], body=body, peer=peer).save()
        except:
            log_exception()

        connection.close()
        return

