from core.utils.test import BaseAPITestCase
from rest_framework import status
from pdb import set_trace as stop


class AuthTestCase(BaseAPITestCase):
    def setUp(self):
        self.headers = self.login()
        self.user_data = {"username": "admin", "password": "admin1234"}
    
    def test_login(self):
        response = self.client.post("/api/login/", data=self.user_data, headers=self.headers)
        access_token = response.json().get("access")
        self.assertTrue(access_token, "Login failed: Access token is empty.")
    
    
    
