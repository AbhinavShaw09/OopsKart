from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from model_bakery import baker
from .models import Product


class ProductViewSetTestCases(APITestCase):
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

    def test_create_valid_product(self):
        url = reverse("product-list")
        resp = self.client.get(url, data=self.valid_payload, format="json")
        self.assertEqual(
            resp.status_code, HTTP_200_OK, "failed to get the product list"
        )