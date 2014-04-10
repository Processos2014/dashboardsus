#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sys
import uuid

from django.conf import settings
from django.db import models
from django.db.models import signals
from django.dispatch.dispatcher import receiver
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)

MESES = (
    ('01', 'Janeiro'),
    ('02', 'Fevereiro'),
    ('03', 'Março'),
    ('04', 'Abril'),
    ('05', 'Maio'),
    ('06', 'Junho'),
    ('07', 'Julho'),
    ('08', 'Agosto'),
    ('09', 'Setembro'),
    ('10', 'Outubro'),
    ('11', 'Novembro'),
    ('12', 'Dezembro'),
)
ANOS = (
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
)
ESTADOS = (
    ("AC", "AC"),
    ("AL", "AL"),
    ("AP", "AP"),
    ("AP", "AP"),
    ("BA", "BA"),
    ("CE", "CE"),
    ("DF", "DF"),
    ("GO", "GO"),
    ("ES", "ES"),
    ("MA", "MA"),
    ("MT", "MT"),
    ("MS", "MS"),
    ("MG", "MG"),
    ("PA", "PA"),
    ("PB", "PB"),
    ("PR", "PR"),
    ("PE", "PE"),
    ("PI", "PI"),
    ("RJ", "RJ"),
    ("RN", "RN"),
    ("RS", "RS"),
    ("RO", "RO"),
    ("RR", "RR"),
    ("SP", "SP"),
    ("SC", "SC"),
    ("SE", "SE"),
    ("TO", "TO"),
)

class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

class Municipio(models.Model):
    codigo = models.CharField(_(u'Código'), max_length=64)
    nome = models.CharField(_(u'Nome'), max_length=64)
    estado = models.CharField(_(u'Estado'), max_length=2, choices=ESTADOS)

    class Meta:
        verbose_name = u'Município'
        verbose_name_plural = u'Municípios'
        app_label = string_with_title('core', u' ')

    def __unicode__(self):
        return '%s' % (self.nome)

class Unidade(models.Model):
    codigo = models.CharField(_(u'Código'), max_length=64)
    municipio = models.ForeignKey(Municipio, verbose_name=_(u'Município'))

    class Meta:
        verbose_name = _(u'Unidade')
        verbose_name_plural = _(u'Unidades')
        app_label = string_with_title('core', u' ')

    def __unicode__(self):
        return '%s' % (self.codigo)

class Area(models.Model):
    codigo = models.CharField(max_length=64)
    unidade = models.ForeignKey(Unidade, verbose_name=_(u'Unidade'))

    class Meta:
        verbose_name = _(u'Área')
        verbose_name_plural = _(u'Áreas')
        app_label = string_with_title('core', u' ')

    def __unicode__(self):
        return u'Município %s - Unidade %s - Área %s' % (self.unidade.municipio.nome, self.unidade.codigo, self.codigo)

class ConsultasMedicas(models.Model):
    area = models.ForeignKey(Area, verbose_name=_(u'Área'))
    mes = models.CharField(_(u'Mês'), choices=MESES, max_length=2)
    ano = models.CharField(_('Ano'), choices=ANOS,max_length=4)

    todos = models.IntegerField(_(' '), max_length=16)

    menor_que_um = models.IntegerField(_('< 1'), max_length=16)
    um_a_quatro = models.IntegerField(_('1 - 4'), max_length=32)
    cinco_a_nove = models.IntegerField(_('5 - 6'), max_length=32)
    dez_a_quatorze = models.IntegerField(_('10 - 14'), max_length=32)
    quinze_a_dezenove = models.IntegerField(_('15 - 19'), max_length=32)
    vinte_a_trinta_e_nove = models.IntegerField(_('20 - 39'), max_length=32)
    quarenta_a_quarenta_e_nove = models.IntegerField(_('40 - 49'), max_length=32)
    cinquenta_a_cinquenta_e_nove = models.IntegerField(_('50 - 59'), max_length=32)
    maior_que_sessenta = models.IntegerField(_('> 60'), max_length=32)

    class Meta:
        unique_together = ('area', 'mes', 'ano',)
        verbose_name = _(u'Consultas Médicas')
        verbose_name_plural = _(u'Consultas Médicas')
        app_label = string_with_title('core', u' ')

    def __unicode__(self):
        return u'Área %s (%s/%s)' % (self.area.codigo, self.mes, self.ano)

class Pacientes(models.Model):
    area = models.ForeignKey(Area, verbose_name=_(u'Área'))
    mes = models.CharField(_(u'Mês'), choices=MESES, max_length=2)
    ano = models.CharField(_('Ano'), choices=ANOS,max_length=4)

    masculino_menor_que_um = models.IntegerField(_('< 1'), max_length=16)
    masculino_um_a_quatro = models.IntegerField(_('1 - 4'), max_length=32)
    masculino_cinco_a_seis = models.IntegerField(_('5 - 6'), max_length=32)
    masculino_sete_a_nove = models.IntegerField(_('7 - 8'), max_length=32)
    masculino_dez_a_quatorze = models.IntegerField(_('10 - 14'), max_length=32)
    masculino_quinze_a_dezenove = models.IntegerField(_('15 - 19'), max_length=32)
    masculino_vinte_a_trinta_e_nove = models.IntegerField(_('20 - 39'), max_length=32)
    masculino_quarenta_a_quarenta_e_nove = models.IntegerField(_('40 - 49'), max_length=32)
    masculino_cinquenta_a_cinquenta_e_nove = models.IntegerField(_('50 - 59'), max_length=32)
    masculino_maior_que_sessenta = models.IntegerField(_('> 60'), max_length=32)

    feminino_menor_que_um = models.IntegerField(_('< 1'), max_length=16)
    feminino_um_a_quatro = models.IntegerField(_('1 - 4'), max_length=32)
    feminino_cinco_a_seis = models.IntegerField(_('5 - 6'), max_length=32)
    feminino_sete_a_nove = models.IntegerField(_('7 - 9'), max_length=32)
    feminino_dez_a_quatorze = models.IntegerField(_('10 - 14'), max_length=32)
    feminino_quinze_a_dezenove = models.IntegerField(_('15 - 19'), max_length=32)
    feminino_vinte_a_trinta_e_nove = models.IntegerField(_('20 - 39'), max_length=32)
    feminino_quarenta_a_quarenta_e_nove = models.IntegerField(_('40 - 49'), max_length=32)
    feminino_cinquenta_a_cinquenta_e_nove = models.IntegerField(_('50 - 59'), max_length=32)
    feminino_maior_que_sessenta = models.IntegerField(_('> 60'), max_length=32)

    familias_cadastradas = models.IntegerField(_(' '), max_length=16)

    class Meta:
        unique_together = ('area', 'mes', 'ano',)
        verbose_name = _(u'Pacientes')
        verbose_name_plural = _(u'Pacientes')
        app_label = string_with_title('core', u' ')

    def __unicode__(self):
        return u'Área %s  (%s/%s)' % (self.area.codigo, self.mes, self.ano)