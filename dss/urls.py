from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sensors.views.home', name='home'),
    # url(r'^dss/', include('dss.foo.urls')),
	url(r'^data/$', 'sensors.views.data_sensores' ),

	url(r'^call_celery/$', 'sensors.views.call_celery' ),

    url(r'^mark_alert/(?P<id>\d+)$', 'sensors.views.mark_alert' ),

    #Url que entrega los datos de un sensor para que se grafique
    url(r'^graph/(?P<id>\d+)$', 'sensors.views.graph' ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
