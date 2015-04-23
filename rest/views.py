from emails.models import *
from rest_framework import viewsets
from rest_framework import filters
from rest.serializers import *


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_fields = ('email', 'sender', 'title', 'time_stamp', 'email__email')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
