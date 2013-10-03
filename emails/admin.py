from django.contrib import admin
from models import *

class UserAdmin(admin.ModelAdmin):
    fields = ['email']
    list_display = ['email']
admin.site.register(User, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    fields = ['email', 'title', 'body']
    list_display = ['email', 'title', 'time_stamp']
admin.site.register(Message, MessageAdmin)
