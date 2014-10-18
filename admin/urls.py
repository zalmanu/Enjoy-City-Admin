from django.conf.urls import patterns, url

urlpatterns = patterns('admin.views',
    url(r'^$', 'home', name='home'),
)
