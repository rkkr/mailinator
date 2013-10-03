from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    
    def __unicode__(self):
        return self.email

class Message(models.Model):
    email = models.ForeignKey(User)
    title = models.CharField(max_length=1024)
    body = models.TextField()
    time_stamp = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.title
