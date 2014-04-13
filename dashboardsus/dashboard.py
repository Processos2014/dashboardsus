#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'dashboardsus.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.AppList(
            _(u'Formulários'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=(
                'dashboardsus.apps.core.models.ConsultasMedicas',
                'dashboardsus.apps.core.models.Pacientes',
            ),
        ))

        self.children.append(modules.AppList(
            _(u'Configuração'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=(
                'dashboardsus.apps.core.models.Municipio',
                'dashboardsus.apps.core.models.Unidade',
                'dashboardsus.apps.core.models.Area',
            ),
        ))

        # self.children.append(modules.Group(
        #     _('Administration'),
        #     column=1,
        #     collapsible=True,
        #     children = [
        #         modules.AppList(
        #             _('General configurations'),
        #             collapsible=False,
        #             column=1,
        #             models=(
        #                 'dashboardsus.apps.core.models.ConsultasMedicas',
        #             ),
        #         ),
        #         modules.AppList(
        #             _('Publication configurations'),
        #             collapsible=False,
        #             column=1,
        #             models=(
        #                 # 'dashboardsus.apps.core.models.Editorial',
        #                 # 'dashboardsus.apps.core.models.Discipline',
        #             ),
        #         ),
        #         modules.AppList(
        #             _('Users'),
        #             column=1,
        #             collapsible=False,
        #             models=('django.contrib.*',),
        #         ),
        #     ]
        # ))

        # self.children.append(modules.LinkList(
        #     _('Pages'),
        #     column=2,
        #     children=[
        #         {
        #             'title': _('Fotec front-end'),
        #             'url': '/home/',
        #             'external': False,
        #         },
        #         # {
        #         #     'title': _('Grappelli Documentation'),
        #         #     'url': 'http://packages.python.org/django-grappelli/',
        #         #     'external': True,
        #         # },
        #         # {
        #         #     'title': _('Grappelli Google-Code'),
        #         #     'url': 'http://code.google.com/p/django-grappelli/',
        #         #     'external': True,
        #         # },
        #     ]
        # ))

        # self.children.append(modules.RecentActions(
        #     title=_('Recent Actions'),
        #     column=2,
        #     collapsible=False,
        #     limit=5,
        # ))



