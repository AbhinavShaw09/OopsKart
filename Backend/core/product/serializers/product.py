from rest_framework import serializers
from ..models import Product, ProductCategory


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    selling_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=200)
    img = serializers.ImageField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all()
    )
    in_stock = serializers.BooleanField(default=True, required=False)
    review_average_rating = serializers.FloatField(required=False)
    review_count = serializers.IntegerField(required=False)

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be blank.")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError(
                "Product name should only contain letters and spaces."
            )
        return value

    def validate_selling_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Product selling price must be greater than zero."
            )
        if value > 100000:
            raise serializers.ValidationError(
                "Product selling price seems unrealistic."
            )
        return value

    def validate_discounted_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Product discounted price must be greater than zero."
            )
        if value > 100000:
            raise serializers.ValidationError("Product price seems unrealistic.")
        return value

    def validate_img(self, value):
        max_file_size = 5 * 1024 * 1024  # 5 MB
        if value and value.size > max_file_size:
            raise serializers.ValidationError(
                "Product image file size should not exceed 5 MB."
            )
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Product description cannot be blank.")
        return value

    def validate_category(self, value):
        if not ProductCategory.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("This product category does not exist")
        return value

    def validate_in_stock(self, value):
        if not value:
            raise serializers.ValidationError("The product is not in stock")
        return value
    
    def validate_review_average_rating(self,value):
        if value is not None and (value < 0 or value > 5):
            raise serializers.ValidationError("The review average rating must be between 0 and 5.")
        return value
    
    def validate_review_count(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("The review count cannot be negative.")
        return value
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.product_img = validated_data.get("product_img", instance.product_img)
        instance.save()
        return instance
