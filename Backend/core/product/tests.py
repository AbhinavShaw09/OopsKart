from core.utils.test import BaseAPITestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from model_bakery import baker
from .models import Product
from pdb import set_trace


class ProductViewSetTestCases(BaseAPITestCase):
    def setUp(self) -> None:
        self.product_data = baker.make(Product)
        self.valid_payload = {
            "name": "New Test Product",
            "description": "An updated product description",
            "price": 15.99,
        }
        self.invalid_payload = {
            "name": "",
            "description": "This is an invalid product",
            "price": -1,
        }
        
        self.headers = self.login()

    def test_create_valid_product(self):
        resp = self.client.get(path="/api/products/", headers=self.headers)
        self.assertEqual(
            resp.status_code, HTTP_200_OK, "failed to get the product list"
        )

    
    