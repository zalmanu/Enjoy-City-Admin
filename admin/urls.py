from django.conf.urls import patterns, url

urlpatterns = patterns('admin.views',
    url(r'^$', 'home', name='home'),
    url(r'^location/(?P<location_id>[0-9a-zA-Z]+)/$', 'location', name='location'),
)
