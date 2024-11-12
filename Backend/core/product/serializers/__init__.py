from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(max_length=50)
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    product_img = serializers.ImageField(required=False, allow_null=True)

    def validate_product_name(self, value):
        """Ensure product_name is not empty and contains only letters and spaces."""
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be blank.")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Product name should only contain letters and spaces.")
        return value

    def validate_product_price(self, value):
        """Ensure product_price is positive and within a realistic range."""
        if value <= 0:
            raise serializers.ValidationError("Product price must be greater than zero.")
        if value > 100000:
            raise serializers.ValidationError("Product price seems unrealistic.")
        return value

    def validate_product_img(self, value):
        """Ensure the product_img file size is within a certain limit (e.g., 5 MB)."""
        max_file_size = 5 * 1024 * 1024  # 5 MB
        if value and value.size > max_file_size:
            raise serializers.ValidationError("Product image file size should not exceed 5 MB.")
        return value

    def create(self, validated_data):
        """Create and return a new Product instance, given the validated data."""
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Product instance, given the validated data."""
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_price = validated_data.get('product_price', instance.product_price)
        instance.product_img = validated_data.get('product_img', instance.product_img)
        instance.save()
        return instance
