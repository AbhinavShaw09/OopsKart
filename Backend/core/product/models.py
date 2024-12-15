from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from core.models import BaseModel
from .constants import (
    ProductCategoryChoices,
    GenderChoices,
    CountryChoices,
    ProductSizeChoices,
)

from rest_framework import serializers


class ProductCategory(BaseModel):
    name = models.IntegerField(
        choices=ProductCategoryChoices.choices(),
        default=ProductCategoryChoices.SPORTS.value,
    )
    description = models.TextField(max_length=300, blank=True, null=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_active_product(cls, category_uuid):
        return Product.objects.filter(category_uuid=category_uuid, is_active=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "ProductCategories"


class Product(BaseModel):
    name = models.CharField(max_length=50)  # By default null=False, blank=False
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    selling_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    description = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to="product_images/", blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    review_average_rating = models.FloatField(null=True)
    review_count = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name

    def clean(self):
        if self.price < 0:
            raise ValidationError("Prices cannot be negative")

    @classmethod
    def get_all_active_product(cls):
        return Product.objects.filter(is_active=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Products"


class ProductDetails(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    dimention = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    data_first_available = models.DateField(default=datetime.now)
    country_of_origin = models.IntegerField(
        choices=CountryChoices.choices(),
        default=CountryChoices.India.value,
    )
    packer = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    importer = models.CharField(max_length=100)
    gender = models.IntegerField(
        choices=GenderChoices.choices(),
        default=GenderChoices.MALE.value,
    )

    def __str__(self):
        return f"{self.product.name}-{self.country_of_origin}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "ProductDetails"


class ProductAttributes(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(null=True, blank=True, max_length=100)
    size = models.IntegerField(
        choices=ProductSizeChoices.choices(),
        default=ProductSizeChoices.lg.value,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "ProductAttributes"
