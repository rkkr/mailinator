from django.conf.urls import  url
import views

urlpatterns = [
    url(r'^$', views.mail_list),
    url(r'mail/(?P<mail_id>\d+)/$', views.mail_view),
]
