#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import *

admin.site.unregister(Group)

class MunicipioAdmin(admin.ModelAdmin):
   model = Municipio
   classes = ('grp-collapse grp-open',)
   inline_classes = ('grp-collapse grp-open',)
   fieldsets = (
       (
           _(u'Município'), {
               'fields' : (
                   'codigo',
                   'nome',
               )
           }
       ),
   )

admin.site.register(Municipio, MunicipioAdmin)

class UnidadeAdmin(admin.ModelAdmin):
   model = Unidade
   classes = ('grp-collapse grp-open',)
   inline_classes = ('grp-collapse grp-open',)
   fieldsets = (
       (
           _(u'Unidade'), {
               'fields' : (
                   'municipio',
                   'codigo',
               )
           }
       ),
   )

admin.site.register(Unidade, UnidadeAdmin)

class AreaAdmin(admin.ModelAdmin):
   model = Area
   classes = ('grp-collapse grp-open',)
   inline_classes = ('grp-collapse grp-open',)
   fieldsets = (
       (
           _(u'Área'), {
               'fields' : (
                   'unidade',
                   'codigo',
               )
           }
       ),
   )

admin.site.register(Area, AreaAdmin)

class ConsultasMedicasAdmin(admin.ModelAdmin):
    model = ConsultasMedicas
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)
    fieldsets = (
        (
            _(u'Informacões do cabeçalho'), {
                'fields' : (
                    ('area', 'mes', 'ano',),
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
    list_display = ('area', 'ano', 'mes')
    list_filter = ('area','mes', 'mes')
    search_fields = ('area','mes', 'mes')
    ordering = ('area', 'ano', 'mes',)

admin.site.register(ConsultasMedicas, ConsultasMedicasAdmin)

class PacientesAdmin(admin.ModelAdmin):
    model = Pacientes
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)
    fieldsets = (
        (
            _(u'Informacões do cabeçalho'), {
                'fields' : (
                    ('area','mes', 'ano',),
                )
            }
        ),
        (
            _(u'Masculino'), {
                'fields' : (
                    'masculino_menor_que_um',
                    'masculino_um_a_quatro',
                    'masculino_cinco_a_seis',
                    'masculino_sete_a_nove',
                    'masculino_dez_a_quatorze',
                    'masculino_quinze_a_dezenove',
                    'masculino_vinte_a_trinta_e_nove',
                    'masculino_quarenta_a_quarenta_e_nove',
                    'masculino_cinquenta_a_cinquenta_e_nove',
                    'masculino_maior_que_sessenta',
                )
            }
        ),
                (
            _(u'Feminino'), {
                'fields' : (
                    'feminino_menor_que_um',
                    'feminino_um_a_quatro',
                    'feminino_cinco_a_seis',
                    'feminino_sete_a_nove',
                    'feminino_dez_a_quatorze',
                    'feminino_quinze_a_dezenove',
                    'feminino_vinte_a_trinta_e_nove',
                    'feminino_quarenta_a_quarenta_e_nove',
                    'feminino_cinquenta_a_cinquenta_e_nove',
                    'feminino_maior_que_sessenta',
                )
            }
        ),
        (
            _(u'Famílias cadastradas'), {
                'fields' : (
                    'familias_cadastradas',
                )
            }
        ),
    )
    list_display = ('area', 'ano', 'mes')
    list_filter = ('area','mes', 'mes')
    search_fields = ('area','mes', 'mes')
    ordering = ('area', 'ano', 'mes',)

admin.site.register(Pacientes, PacientesAdmin)