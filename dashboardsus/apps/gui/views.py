#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from django.views.generic import View

logger = logging.getLogger(__name__)

from dashboardsus.apps.core.views import GenericView
from dashboardsus.apps.core.models import (
    Pacientes,
    ConsultasMedicas,
    Municipio,
    Unidade,
    Area
)
class GUI(GenericView):
    def home(self, request):
        relatorios_de_pacientes = Pacientes.objects.all()

        quantidade_de_homens = 0
        quantidade_de_mulheres = 0

        for relatorio in relatorios_de_pacientes:
            quantidade_de_homens += (
                int(relatorio.masculino_menor_que_um) + \
                int(relatorio.masculino_um_a_quatro) + \
                int(relatorio.masculino_cinco_a_seis) + \
                int(relatorio.masculino_sete_a_nove) + \
                int(relatorio.masculino_dez_a_quatorze) + \
                int(relatorio.masculino_quinze_a_dezenove) + \
                int(relatorio.masculino_vinte_a_trinta_e_nove) + \
                int(relatorio.masculino_quarenta_a_quarenta_e_nove) + \
                int(relatorio.masculino_cinquenta_a_cinquenta_e_nove) + \
                int(relatorio.masculino_maior_que_sessenta)
            )

            quantidade_de_mulheres += (
                int(relatorio.feminino_menor_que_um) + \
                int(relatorio.feminino_um_a_quatro) + \
                int(relatorio.feminino_cinco_a_seis) + \
                int(relatorio.feminino_sete_a_nove) + \
                int(relatorio.feminino_dez_a_quatorze) + \
                int(relatorio.feminino_quinze_a_dezenove) + \
                int(relatorio.feminino_vinte_a_trinta_e_nove) + \
                int(relatorio.feminino_quarenta_a_quarenta_e_nove) + \
                int(relatorio.feminino_cinquenta_a_cinquenta_e_nove) + \
                int(relatorio.feminino_maior_que_sessenta)
            )

        return {
            'template' : {
                'homens' : quantidade_de_homens,
                'mulheres' : quantidade_de_mulheres,
            }
        }