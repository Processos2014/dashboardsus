#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import *

admin.site.unregister(Group)

class ConsultasMedicasAdmin(admin.ModelAdmin):
    model = ConsultasMedicas
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)
    fieldsets = (
        (
            _(u'Informacões do cabeçalho'), {
                'fields' : (
                    ('mes', 'ano',),
                )
            }
        ),
        (
            _(u'Residentes fora da área de abrangência'), {
                'fields' : (
                    'todos',
                )
            },
        ),
        (
            _(u'Residentes na área de abrangência da equipe'), {
                'fields' : (
                    'menor_que_um',
                     'um_a_quatro',
                     'cinco_a_nove',
                     'dez_a_quatorze',
                     'quinze_a_dezenove',
                     'vinte_a_trinta_e_nove',
                     'quarenta_a_quarenta_e_nove',
                     'cinquenta_a_cinquenta_e_nove',
                     'maior_que_sessenta',
                )
            }
        ),
    )
    list_display = ('mes', 'ano')
    list_filter = ('mes',)
    search_fields = ('mes',)
    ordering = ('mes', 'ano',)

admin.site.register(ConsultasMedicas, ConsultasMedicasAdmin)
