from django.db import models
import cgi

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    
    def __unicode__(self):
        return self.email

class Message(models.Model):
    email = models.ForeignKey(User, related_name='inbox')
    sender = models.ForeignKey(User, related_name='outbox')
    title = models.CharField(max_length=1024)
    body = models.TextField()
    peer = models.CharField(max_length=255)
    time_stamp = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.title

    def title_clean(self):
        return cgi.escape(self.title) if self.title else 'No title'
