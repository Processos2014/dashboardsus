from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver

class MySeleniumTests(LiveServerTestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.selenium = webdriver.Firefox()
    #     super(MySeleniumTests, cls).setUpClass()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('%s%s' % (self.live_server_url, '/home/'))

    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.selenium.quit()
    #     super(MySeleniumTests, cls).tearDownClass()


    def test_open_system(self):
        enter_link = self.driver.find_element_by_link_text('Inicio')
        self.assertEquals(self.driver.current_url, 'http://localhost:8081/home/')

    def test_route_for_login_page(self):
        enter_link = self.driver.find_element_by_link_text('Entrar')
        enter_link.click()

        login_page_body = self.driver.find_element_by_tag_name('body')

        self.driver.implicitly_wait(10)

        self.assertEquals(self.driver.current_url, 'http://localhost:8081/accounts/logon/')

        # self.assertIn('Entar no Dashboard SUS', login_page_body.text)

    def test_login(self):

        enter_link = self.driver.find_element_by_link_text('Entrar')
        enter_link.click()

        login_input = self.driver.find_element_by_id('username')
        login_input.send_keys('admin')

        password_input = self.driver.find_element_by_id('password')
        password_input.send_keys('admin')

        form_button = self.driver.find_element_by_id('submit')
        form_button.click()

        self.driver.implicitly_wait(10)

        enter_link = self.driver.find_element_by_link_text('Inicio')
        enter_link.click()

        self.assertEquals(self.driver.current_url, 'http://localhost:8081/home/')

    # def test_route_from_enter_back_to_index(self):
        # enter_link = self.selenium.find_element_by_link_text('Entrar')
        # enter_link.click()
        # self.selenium.implicitly_wait(2)

        # home_link = self.selenium.find_element_by_link_text('Inicio')
        # home_link.click

        # home_link = self.selenium.find_element_by_link_text('Inicio')
        # home_link.click

        # self.assertEquals(self.selenium.current_url, '/home/')

