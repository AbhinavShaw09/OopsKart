from core.utils.test import BaseAPITestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from model_bakery import baker
from .models import Product, ProductCategory


class ProductViewSetTestCases(BaseAPITestCase):
    def setUp(self) -> None:
        self.product_data = baker.make(Product)
        self.product_category = baker.make(ProductCategory)
        self.valid_payload = {
            "name": "Example Product",
            "original_price": 100.50,
            "selling_price": 90.00,
            "discounted_price": 80.00,
            "description": "A sample product description.",
            "category": self.product_category.id,
            "in_stock": True,
            "review_average_rating": 4.5,
            "review_count": 10,
        }

        self.invalid_payload = {
            "name": "",
            "description": "This is an invalid product",
            "price": -1,
        }
        self.headers = self.login()

    def test_create_product(self):
        resp = self.client.post(
            path="/api/create-product/",
            headers=self.headers,
            data=self.valid_payload,
        )
        self.assertEqual(
            resp.status_code, HTTP_201_CREATED, "Failed to create a product"
        )
        self.assertIn("id", resp.json())

    def test_list_product(self):
        resp = self.client.get(path="/api/products/", headers=self.headers)
        self.assertEqual(
            resp.status_code, HTTP_200_OK, "Failed to get the product list"
        )
