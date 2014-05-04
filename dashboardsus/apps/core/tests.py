rom django.test import TestCase, Client
from dashboardsus.apps.accounts.models import CustomUser
from dashboardsus.apps.core.models import Municipio

class CoreTests(TestCase):
    def setUp(self):
        user = CustomUser.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_municipio_can_be_created_with_no_parameters(self):
        Municipio.objects.create()
        self.assertEqual(Municipio.objects.count(), 1)

    def test_home_route(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 301)

# Create your tests here.