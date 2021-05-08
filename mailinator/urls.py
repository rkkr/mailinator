from django.conf.urls import include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mailinator.views.home', name='home'),
    # url(r'^mailinator/', include('mailinator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest/', include('rest.urls')),
    url(r'^', include('emails.urls')),
]
