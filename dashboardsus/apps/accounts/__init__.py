#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db import models
from django.db.models import signals

from dashboardsus.apps.accounts.models import CustomUser

signals.post_syncdb.disconnect(create_superuser, sender=auth_models, dispatch_uid='django.contrib.auth.management.create_superuser')

def create_admin(app, created_models, verbosity, **kwargs):

    username = 'admin'
    password = 'admin'
    cpf = '00000000000'
    email = 'integrasis@basecorp.com.br'
    first_name = 'Administrador'
    last_name = 'Administrador'

    try:
        CustomUser.objects.get(username='admin')
    except CustomUser.DoesNotExist:
        print ''
        print '-' * 80
        print 'Creating admin user with login: %s and password: %s' % (username, password)
        print '-' * 80
        print ''
        assert CustomUser.objects.create_superuser(
            username=username,
            password=password,
            email=email,
            cpf=cpf,
            first_name=first_name,
            last_name=last_name,
        )

signals.post_syncdb.connect(create_admin, sender=auth_models, dispatch_uid='apps.auth.models.create_admin')