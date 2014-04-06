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

class ConsultasMedicas(models.Model):
    # area = models.ForeignKey(Area, verbose_name=_('Área'))
    mes = models.CharField(_(u'Mês'), choices=MESES, max_length=2)
    ano = models.CharField(_('Ano'), choices=ANOS,max_length=4)

    todos = models.CharField(_(' '), max_length=16)

    menor_que_um = models.CharField(_('< 1'), max_length=16)
    um_a_quatro = models.CharField(_('1 - 4'), max_length=32)
    cinco_a_nove = models.CharField(_('5 - 6'), max_length=32)
    dez_a_quatorze = models.CharField(_('10 - 14'), max_length=32)
    quinze_a_dezenove = models.CharField(_('15 - 19'), max_length=32)
    vinte_a_trinta_e_nove = models.CharField(_('20 - 39'), max_length=32)
    quarenta_a_quarenta_e_nove = models.CharField(_('40 - 49'), max_length=32)
    cinquenta_a_cinquenta_e_nove = models.CharField(_('50 - 59'), max_length=32)
    maior_que_sessenta = models.CharField(_('> 60'), max_length=32)

    class Meta:
        unique_together = ('mes', 'ano',)
        verbose_name = _('Consultas Medicas')
        verbose_name_plural = _('Consultas Medicas')

    def __unicode__(self):
        return u'%s contact' % (self.type.capitalize())
