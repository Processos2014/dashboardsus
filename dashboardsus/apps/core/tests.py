from django.test import TestCase, Client
from dashboardsus.apps.accounts.models import CustomUser
from dashboardsus.apps.core.models import *

class CoreTests(TestCase):
    def setUp(self):
        #user = CustomUser.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        pass

    def test_municipio_can_be_created_with_no_parameters(self):
        Municipio.objects.create()
        self.assertEqual(Municipio.objects.count(), 1)

    def test_redirect_home_route(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 301)

    def test_home_route(self):
        c = Client()
        response = c.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_access_wighout_logon(self):
        c = Client()
        response = c.get('/admin/core/consultasmedicas/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_on_login(self):
        c = Client()
        response = c.post('/admin/', {'username' : 'admin', 'password' : 'admin'})
        self.assertEqual(response.status_code, 200)

        response = c.get('/admin/core/consultasmedicas/')
        self.assertEqual(response.status_code, 200)


# Create your tests here.