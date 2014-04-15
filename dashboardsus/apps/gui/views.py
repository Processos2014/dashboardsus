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
    Area,
)

class GUI(GenericView):
    def home(self, request):
        municipios = Municipio.objects.all()
        unidades = Unidade.objects.all()
        areas = Area.objects.all()
        relatorios_de_pacientes = Pacientes.objects.all()
        relatorio_consultas_medicas = ConsultasMedicas.objects.all()

        try:
            municipio = request.GET['municipio']
        except Exception, e:
            municipio = None
            print str(e)
        else:
            if municipio != "":
                municipio = Municipio.objects.get(pk = municipio)
                areas = Area.objects.filter(unidade__municipio = municipio)
                relatorios_de_pacientes = relatorios_de_pacientes.filter(area__in = areas)
                relatorio_consultas_medicas = relatorio_consultas_medicas.filter(area__in = areas)
            else:
                municipio = None

        try:
            unidade = request.GET['unidade']
        except Exception, e:
            unidade = None
            print str(e)
        else:
            if unidade != "":
                unidade = Unidade.objects.get(pk = unidade)
                areas = Area.objects.filter(unidade = unidade)
                relatorios_de_pacientes = relatorios_de_pacientes.filter(area__in = areas)
                relatorio_consultas_medicas = relatorio_consultas_medicas.filter(area__in = areas)
            else:
                unidade = None

        try:
            area = request.GET['area']
        except Exception, e:
            area = None
            print str(e)
        else:
            if area != "":
                area = Area.objects.get(pk = area)
                relatorios_de_pacientes = relatorios_de_pacientes.filter(area = area)
                relatorio_consultas_medicas = relatorio_consultas_medicas.filter(area = area)
            else:
                area = None

        try:
            ano = request.GET['ano']
        except Exception, e:
            ano = None
            print str(e)
        else:
            if ano != "":
                relatorios_de_pacientes = relatorios_de_pacientes.filter(ano = ano)
                relatorio_consultas_medicas = relatorio_consultas_medicas.filter(ano = ano)
            else:
                ano = None

        try:
            mes = request.GET['mes']
        except Exception, e:
            mes = None
            print str(e)
        else:
            if mes != "":
                relatorios_de_pacientes = relatorios_de_pacientes.filter(mes = mes)
                relatorio_consultas_medicas = relatorio_consultas_medicas.filter(mes = mes)
            else:
                mes = None

        quantidade_de_homens = 0
        quantidade_de_mulheres = 0
        quantidade_fora_area_abrangencia = 0
        quantidade_area_abrangencia = 0
        dicionario_homens_faixa_etaria = []
        dicionario_mulheres_faixa_etaria = []

        for relatorio in relatorio_consultas_medicas:
            quantidade_area_abrangencia += (
                int(relatorio.menor_que_um) + \
                int(relatorio.um_a_quatro) + \
                int(relatorio.cinco_a_nove) + \
                int(relatorio.dez_a_quatorze) + \
                int(relatorio.quinze_a_dezenove) + \
                int(relatorio.vinte_a_trinta_e_nove) + \
                int(relatorio.quarenta_a_quarenta_e_nove) + \
                int(relatorio.cinquenta_a_cinquenta_e_nove) + \
                int(relatorio.maior_que_sessenta)
            )

            quantidade_fora_area_abrangencia += (
                int(relatorio.todos)
            )

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

            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_menor_que_um))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_um_a_quatro))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_cinco_a_seis))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_sete_a_nove))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_dez_a_quatorze))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_quinze_a_dezenove))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_vinte_a_trinta_e_nove))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_quarenta_a_quarenta_e_nove))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_cinquenta_a_cinquenta_e_nove))
            dicionario_homens_faixa_etaria.append(int(relatorio.masculino_maior_que_sessenta))

            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_menor_que_um))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_um_a_quatro))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_cinco_a_seis))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_sete_a_nove))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_dez_a_quatorze))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_quinze_a_dezenove))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_vinte_a_trinta_e_nove))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_quarenta_a_quarenta_e_nove))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_cinquenta_a_cinquenta_e_nove))
            dicionario_mulheres_faixa_etaria.append(int(relatorio.feminino_maior_que_sessenta))

        return {
            'template' : {
                'homens' : quantidade_de_homens,
                'mulheres' : quantidade_de_mulheres,
                'qtd_dentro' : quantidade_area_abrangencia,
                'qtd_fora' : quantidade_fora_area_abrangencia,
                'dic_homens': dicionario_homens_faixa_etaria,
                'dic_mulheres': dicionario_mulheres_faixa_etaria,
                'municipios' : municipios,
                'unidades' : unidades,
                'areas' : areas,
                'municipio' : municipio,
                'unidade' : unidade,
                'area' : area,
                'mes' : mes,
                'ano' : ano,
            }
        }

    def pacientes(self, request):
        pacientes = Pacientes.objects.all()


        return {
            'template' : {
                'pacientes' : pacientes,
            }
        }


    def adicionar_pacientes(self, request):
        data = None

        if request.method == 'POST':
            try:
                data = self.load_json(request.POST['data'])
                area = self.load_json(request.POST['area'])
                mes = self.load_json(request.POST['mes'])
                ano = self.load_json(request.POST['ano'])
                familias_cadastradas = self.load_json(request.POST['familias_cadastradas'])
            except Exception, e:
                data = {
                    'leftover' : {
                        'alert-error' : 'Não foi possível completar a solicitação!',
                    }
                }
            else:
                try:
                    pacientes = Pacientes()
                    pacientes.area = Area.objects.get(pk = area)
                    pacientes.mes = mes
                    pacientes.ano = ano
                    pacientes.familias_cadastradas = familias_cadastradas

                    pacientes.masculino_menor_que_um = data[0][0]
                    pacientes.masculino_um_a_quatro = data[1][0]
                    pacientes.masculino_cinco_a_seis = data[2][0]
                    pacientes.masculino_sete_a_nove = data[3][0]
                    pacientes.masculino_dez_a_quatorze = data[4][0]
                    pacientes.masculino_quinze_a_dezenove = data[5][0]
                    pacientes.masculino_vinte_a_trinta_e_nove = data[6][0]
                    pacientes.masculino_quarenta_a_quarenta_e_nove = data[7][0]
                    pacientes.masculino_cinquenta_a_cinquenta_e_nove = data[8][0]
                    pacientes.masculino_maior_que_sessenta = data[9][0]

                    pacientes.feminino_menor_que_um = data[0][1]
                    pacientes.feminino_um_a_quatro = data[1][1]
                    pacientes.feminino_cinco_a_seis = data[2][1]
                    pacientes.feminino_sete_a_nove = data[3][1]
                    pacientes.feminino_dez_a_quatorze = data[4][1]
                    pacientes.feminino_quinze_a_dezenove = data[5][1]
                    pacientes.feminino_vinte_a_trinta_e_nove = data[6][1]
                    pacientes.feminino_quarenta_a_quarenta_e_nove = data[7][1]
                    pacientes.feminino_cinquenta_a_cinquenta_e_nove = data[8][1]
                    pacientes.feminino_maior_que_sessenta = data[9][1]

                    pacientes.save()

                except Exception, e:
                    data = {
                        'leftover' : {
                            'alert-error' : 'Não foi possível completar a solicitação (error: %s)' % str(e),
                        }
                    }
                else:
                    data = {
                        'leftover' : {
                            'alert-success' : 'Salvo com sucesso!',
                            'redirect' : '/pacientes/',
                        }
                    }

            finally:
                return data

        else:
            areas = Area.objects.all()

            return {
                'template' : {
                    'areas' : areas,
                }
            }

    def editar_pacientes(self, request):
        data = None

        if request.method == 'POST':
            try:
                pk = self.kwargs['pk']
                data = self.load_json(request.POST['data'])
                area = self.load_json(request.POST['area'])
                mes = self.load_json(request.POST['mes'])
                ano = self.load_json(request.POST['ano'])
                familias_cadastradas = self.load_json(request.POST['familias_cadastradas'])

                pacientes = Pacientes.objects.get(pk = pk)
            except Exception, e:
                data = {
                    'leftover' : {
                        'alert-error' : 'Não foi possível completar a solicitação!',
                    }
                }
            else:
                try:
                    pacientes.area = Area.objects.get(pk = area)
                    pacientes.mes = mes
                    pacientes.ano = ano
                    pacientes.familias_cadastradas = familias_cadastradas

                    print data[1][0]
                    pacientes.masculino_menor_que_um = data[0][0]
                    pacientes.masculino_um_a_quatro = data[1][0]
                    pacientes.masculino_cinco_a_seis = data[2][0]
                    pacientes.masculino_sete_a_nove = data[3][0]
                    pacientes.masculino_dez_a_quatorze = data[4][0]
                    pacientes.masculino_quinze_a_dezenove = data[5][0]
                    pacientes.masculino_vinte_a_trinta_e_nove = data[6][0]
                    pacientes.masculino_quarenta_a_quarenta_e_nove = data[7][0]
                    pacientes.masculino_cinquenta_a_cinquenta_e_nove = data[8][0]
                    pacientes.masculino_maior_que_sessenta = data[9][0]

                    pacientes.feminino_menor_que_um = data[0][1]
                    pacientes.feminino_um_a_quatro = data[1][1]
                    pacientes.feminino_cinco_a_seis = data[2][1]
                    pacientes.feminino_sete_a_nove = data[3][1]
                    pacientes.feminino_dez_a_quatorze = data[4][1]
                    pacientes.feminino_quinze_a_dezenove = data[5][1]
                    pacientes.feminino_vinte_a_trinta_e_nove = data[6][1]
                    pacientes.feminino_quarenta_a_quarenta_e_nove = data[7][1]
                    pacientes.feminino_cinquenta_a_cinquenta_e_nove = data[8][1]
                    pacientes.feminino_maior_que_sessenta = data[9][1]

                    pacientes.save()

                except Exception, e:
                    data = {
                        'leftover' : {
                            'alert-error' : 'Não foi possível completar a solicitação (error: %s)' % str(e),
                        }
                    }
                else:
                    data = {
                        'leftover' : {
                            'alert-success' : 'Salvo com sucesso!',
                            'redirect' : '/pacientes/',
                        }
                    }

            finally:
                return data
        else:
            try:
                pk = self.kwargs['pk']
                pacientes = Pacientes.objects.get(pk = pk)
            except Exception, e:
                data = {
                    'leftover' : {
                        'alert-error' : 'Ocorreu algum erro (erro %s).' % str(e),
                    }
                }
            else:
                areas = Area.objects.all()

                data_table = []

                row = []
                row.append(pacientes.masculino_menor_que_um)
                row.append(pacientes.feminino_menor_que_um)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_um_a_quatro)
                row.append(pacientes.feminino_um_a_quatro)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_cinco_a_seis)
                row.append(pacientes.feminino_cinco_a_seis)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_sete_a_nove)
                row.append(pacientes.feminino_sete_a_nove)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_dez_a_quatorze)
                row.append(pacientes.feminino_dez_a_quatorze)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_quinze_a_dezenove)
                row.append(pacientes.feminino_quinze_a_dezenove)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_vinte_a_trinta_e_nove)
                row.append(pacientes.feminino_vinte_a_trinta_e_nove)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_quarenta_a_quarenta_e_nove)
                row.append(pacientes.feminino_quarenta_a_quarenta_e_nove)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_cinquenta_a_cinquenta_e_nove)
                row.append(pacientes.feminino_cinquenta_a_cinquenta_e_nove)
                data_table.append(row)
                row = []
                row.append(pacientes.masculino_maior_que_sessenta)
                row.append(pacientes.feminino_maior_que_sessenta)
                data_table.append(row)

                data = {
                    'template' : {
                        'areas' : areas,
                        'pacientes' : pacientes,
                        'data_table' : data_table,
                    }
                }
            finally:
                return data

    def deletar_pacientes(self, request):
        data = None

        try:
            pk = self.kwargs['pk']
            Pacientes.objects.get(pk = pk).delete()
        except Exception, e:
            data = {
                'leftover' : {
                    'alert-error' : 'Ocorreu algum erro (erro %s).' % str(e),
                }
            }
        else:
            data = {
                'leftover' : {
                    'alert-success' : 'Deletado com sucesso!',
                }
            }
        finally:
            return data