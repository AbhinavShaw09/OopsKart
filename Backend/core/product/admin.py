from django.contrib import admin
from .models import Product, ProductCategory, ProductDetails, ProductAttributes

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductDetails)
admin.site.register(ProductAttributes)

