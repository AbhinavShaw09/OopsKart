from .models import Product
from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path("products/", ProductViewSet.as_view({"get": "list"}), name="product-list"),
    path(
        "create-product/", ProductViewSet.as_view({"post": "create_product"}), name="create-product"
    ),
]
