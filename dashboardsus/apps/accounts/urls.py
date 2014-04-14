#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import RedirectView

from views import AccountsView

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='/accounts/logon/'), name='accounts',),
	url(r'^(?P<slug>\w+)/$', AccountsView.as_view(), name='accounts',),
	url(r'^accounts/(?P<slug>\w+)/$', AccountsView.as_view(), name='accounts',),
	url(r'^accounts/(?P<slug>\w+)/(?P<key>\d+)/$', AccountsView.as_view(), name='accounts',),
)