from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

from apps.gui.views import GUI

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboardsus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url='/home/')),

    url(r'^(?P<slug>\w+)/$', GUI.as_view(), name='gui',),
)
