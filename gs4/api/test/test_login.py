# from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Account


class LoginAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        Accounts= Account.objects.create_user(
            username="Ayush",
            email="ayush@example.com",
            password="testpassword123"
        )
        # Create an account linked with this user
        self.account = Account.objects.create(
            account_name="Test Account"
        )
        self.account.users.add(self.user)

        self.login_url = reverse("login")  # your login endpoint name

    def test_login_with_valid_credentials(self):
        """User can login with correct username & password"""
        data = {"username": "ayush", "password": "testpassword123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)  # if JWT/session returns token

    def test_login_with_invalid_password(self):
        """Login fails with wrong password"""
        data = {"username": "ayush", "password": "wrongpass"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_nonexistent_user(self):
        """Login fails for non-existing user"""
        data = {"username": "ghost", "password": "testpassword123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
