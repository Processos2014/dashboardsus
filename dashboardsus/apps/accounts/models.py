#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
import re

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager)
from django.core.mail import send_mail
from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    A custom user class that basically mirrors Django's `AbstractUser` class
    and doesn't force `first_name` or `last_name` with sensibilities for
    international names.

    http://www.w3.org/International/questions/qa-personal-names
    """
    username = models.CharField(
        _('Username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ]
    )
    first_name = models.CharField(
        _('First name'),
        max_length=254,
        blank=True,
        help_text=_('First name.'),

    )
    last_name = models.CharField(
        _('Last name'),
        max_length=30,
        blank=True,
        help_text=_('Last name.'),
    )
    email = models.EmailField(
        _('E-mail'),
        max_length=254,
        unique=True,
        help_text=_('E-mail.'),
    )
    cpf = models.CharField(
        _('CPF'),
        max_length=11,
        null=False,
        help_text=_('CPF.'),
    )
    is_staff = models.BooleanField(
        _('Staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('Active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(
        _('Date joined'),
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'cpf',
        'email',
    ]

    class Meta:
        verbose_name = 'colaborador' # Translation not found to 'colaborador'
        verbose_name_plural = 'colaboradores' # Translation not found to 'colaboradores'

    def __unicode__(self):
        return self.username

    def get_short_name(self):
        return self.first_name