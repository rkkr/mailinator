from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.mail_list),
    url(r'mail/(?P<mail_id>\d+)/$', views.mail_view),
)
