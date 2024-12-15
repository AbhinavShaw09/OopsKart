from rest_framework.test import APITestCase

class BaseAPITestCase(APITestCase):    
    def login(self):
        user_data = {"username": "admin", "password": "admin1234"}
        resp = self.client.post("/api/signup/", data=user_data)
        token = resp.json()["access"]
        headers = {"Authorization": f"Bearer {token}"}
        return headers
    

