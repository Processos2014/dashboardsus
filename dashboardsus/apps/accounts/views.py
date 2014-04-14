#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.contrib.auth import authenticate, login, logout

from dashboardsus.apps.core.views import GenericView

class AccountsView(GenericView):
	'''
	'''
	def update(self, request):
		if request.method == 'POST':
			try:
				first_name = request.POST['first_name']
				last_name = request.POST['last_name']
				password = request.POST['password']
				password2 = request.POST['password2']
			except Exception, e:
				logger.error(str(e))

				data = {
					'leftover' : {
						'alert-error' : 'Não foi possível processar esta operação!',
						'redirect' : 'none',
					}
				}
			else:

				if not first_name != '':
					data = {
						'leftover' : {
							'alert-error' : 'Digite o nome completo!',
							'redirect' : 'none',
						}
					}
				elif not password == password2:
					data = {
						'leftover' : {
							'alert-error' : 'Senhas não conferem!',
							'redirect' : 'none',
						}
					}
				else:
					try:
						request.user.first_name = first_name
						request.user.last_name = last_name
						if password2 != '':
							request.user.set_password(password2)
						request.user.save()
					except Exception, e:
						logger.error(str(e))

					data = {
						'leftover' : {
							'alert-success' : 'Dados salvos com sucesso!',
							'redirect' : 'none',
						}
					}

			finally:
				return data

	def logon(self, request):

		if request.user.is_authenticated():
			return {
				'leftover' : {
					'redirect' : '/home/'
				}
			}
		elif request.method == 'POST':
			try:
				username = request.POST['username']
				password = request.POST['password']
			except Exception, e:
				logger.error('Required fields aren\'t defined! Raised: ' + str(e))

				data = {
					'leftover' : {
						'alert-error' : 'Nome de usuário e/ou senha não foram definidos!',
						'redirect' : 'none'
					}
				}
			else:
				try:
					authenticated_user = authenticate(username=username, password=password)
				except Exception, e:
					logger.error('Can\'t authenticate user! Raised : ' + str(e))

					data = {
						'leftover' : {
							'alert-error' : 'Usuário não pode ser autenticado!',
							'redirect' : 'none',
						}
					}
				else:
					if authenticated_user == None:
						data = {
							'leftover' : {
								'alert-error' : 'O nome de usuário informado e/ou senha estão incorretos, verifique, por favor.',
								'redirect' : 'none',
							}
						}
					elif authenticated_user.is_active:
						login(request, authenticated_user)

						data = {
							'leftover' : {
								'redirect' : '/home/'
							}
						}
					else:
						data = {
							'leftover' : {
								'alert-error' : 'Usuário não está ativo no sistema, entre em contato com o administrador para saber o motivo do ocorrido!',
								'redirect' : 'none',
							}
						}
			finally:
				return data
		else:
			return None

	def logoff(self, request):
		logout(request)

		return {
			'leftover' : {
				'redirect' : '/accounts/logon/',
			}
		}