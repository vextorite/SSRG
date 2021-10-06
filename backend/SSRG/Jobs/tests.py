from django.test import TestCase
from Jobs.models import Jobs, SingleFiles


class URLTests(TestCase):
    """
    A class containing unit tests for url routing, used by Django tests

    
    """
    def testHomePage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testRegisterPage(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
    
    def testLoginPage(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def testNewJobPage(self):
        response = self.client.get('/newJob')
        self.assertEqual(response.status_code, 302)

    def testViewJobsPage(self):
        response = self.client.get('/viewJobs')
        self.assertEqual(response.status_code, 302)

    def testPasswordPage(self):
        response = self.client.get('/password/')
        self.assertEqual(response.status_code, 302)

    def testMenuPage(self):
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 302)

    def testprofilePage(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 302)

class TestSSRGModels(TestCase):
    pass