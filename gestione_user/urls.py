from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from fewclues.gestione_user.views import registrazione
urlpatterns = patterns('',
    url(r'^login', login),
    url(r'^logout', logout),
    url(r'^register', registrazione),
)
