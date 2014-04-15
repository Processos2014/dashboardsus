from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

from apps.gui.views import GUI

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('dashboardsus.apps.accounts.urls', app_name='accounts'), name='accounts'),

    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^(?P<slug>\w+)/$', GUI.as_view(), name='gui',),
    url(r'^(?P<slug>\w+)/(?P<pk>\d+)/$', GUI.as_view(), name='gui',),
    url(r'^(?P<slug>\w+)/search$', GUI.as_view(), name='gui',),
)
