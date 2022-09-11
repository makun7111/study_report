from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path= r'C:\Users\81802\Downloads\chromedriver_win32\chromedriver.exe')
    @classmethod
    def tearĐownClass(cls):
        cls.selenium.quit()
        super().teardownClass()
    def test_login(self):

        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))
        username_input=self.selenium.find_element_by_name("login")
        username_input.send_keys('makun1010it@gmail.com')
        password_input=self.selenium.find_element_by_name("password")
        password_input.send_keys('Maumau1010')
        self.selenium.find_element_by_class_name('btn').click()
        self.assertEquals('日記一覧| Private Diary', self.selenium.title)

