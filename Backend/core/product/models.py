from django.db import models
from django.core.exceptions import ValidationError
from core.models import BaseModel

class Product(BaseModel):
    product_name = models.CharField(max_length = 50, blank=False, null=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_img = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self) -> str:
        return self.product_name

    def clean(self):
        if self.product_price < 0:
            raise ValidationError("Prices cannot be negative")

    class Meta:
        ordering = ['product_name']
        verbose_name_plural = "Products"
