from django.conf.urls.defaults import *
from fewclues.qualcheindizio.views import hello, QualcheindizioMain

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fewclues.views.home', name='home'),
    # url(r'^fewclues/', include('fewclues.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'(\d{1,2})/$', QualcheindizioMain),
#    url(r'^prova/$', prova),
#    url(r'^login/$', login),
)
