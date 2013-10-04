from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register(r'emails', views.EmailViewSet)
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
