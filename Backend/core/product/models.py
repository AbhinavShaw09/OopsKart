from django.db import models
from django.core.exceptions import ValidationError
from core.models import BaseModel
from .enums import ProductCategoryChoices


class ProductCategory(BaseModel):
    name = models.IntegerField(
        choices=[(tag.value, tag.name) for tag in ProductCategoryChoices],
        default=ProductCategoryChoices.SPORTS.value,
    )
    description = models.CharField(max_length=300, blank=True, null=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_active_product(cls, category_uuid):
        return Product.objects.filter(category_uuid=category_uuid, is_active=True)


class Product(BaseModel):
    name = models.CharField(max_length=50)  # By default null=False, blank=False
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
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

    class Meta:
        ordering = ["product_name"]
        verbose_name_plural = "Products"
