from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token 


# SOME RULES:
# 1. if there are multiple test files, create a folder called "tests"
# 2. name all of the test-functions starting with 'test_', like-> 'def test_register(self):'
# 3. if there needs to be some pre-populated data, create then into 'def setUp(self):' function

class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "newuser",
            "email": "newuser@email.com",
            "password": "newuser",
            "password2": "newuser"
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class LoginLogoutTestCase(APITestCase):
    # pre-populating data into the 'setUp(self)' function
    def setUp(self):
        self.user = User.objects.create_user(
            username="testUser",
            password="testUser"
        )
    
    def test_login(self):
        data = {
            "username": "testUser",
            "password": "testUser"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logout(self):
        self.token = Token.objects.get(user__username="testUser").key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)