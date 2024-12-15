from datetime import date

from rest_framework import serializers

from .models import Product, ProductCategory, ProductDetails

from .constants import (
    ProductCategoryChoices,
    GenderChoices,
    CountryChoices,
    ProductSizeChoices,
)


class ProductCategorySerializer(serializers.Serializer):
    name = serializers.ChoiceField(choices=ProductCategoryChoices.choices())
    description = serializers.CharField(
        max_length=300, required=False, allow_blank=True
    )
    in_stock = serializers.BooleanField()

    def validate_name(self, value):
        if value is None:
            raise serializers.ValidationError("Invalid name of product category")
        if value not in ProductCategoryChoices.values():
            raise serializers.ValidationError("Product category choice does not exist")
        return value

    def validate_in_stock(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError(
                "The 'in_stock' field must be a boolean value."
            )
        return value


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    original_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    selling_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=200)
    img = serializers.ImageField(required=False)
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

    def validate_original_price(self, value):
        discounted_price = self.initial_data.get("discounted_price")
        selling_price = self.initial_data.get("selling_price")

        discounted_price = self.is_valid_float_value(discounted_price)
        selling_price = self.is_valid_float_value(selling_price)

        if value <= 0:
            raise serializers.ValidationError(
                "Product selling price must be greater than zero."
            )
        elif value > 100000:
            raise serializers.ValidationError(
                "Product selling price seems unrealistic."
            )
        elif value <= discounted_price:
            raise serializers.ValidationError(
                "Product dicounted price should be higher than its original price"
            )
        elif value <= selling_price:
            raise serializers.ValidationError(
                "Product selling price should be higher than its original price"
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

    def validate_img(self, img):
        if img:
            max_file_size = 5 * 1024 * 1024  # 5 MB
            if img and img.size > max_file_size:
                raise serializers.ValidationError(
                    "Product image file size should not exceed 5 MB."
                )
            return img

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

    def validate_review_average_rating(self, value):
        if value is not None and (value < 0 or value > 5):
            raise serializers.ValidationError(
                "The review average rating must be between 0 and 5."
            )
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

    def is_valid_float_value(self, value):
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise serializers.ValidationError("Discounted value must be a number.")
        return value


class ProductDetailSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=ProductDetails.objects.all())
    dimension = serializers.IntegerField(required=False)
    weight = serializers.IntegerField(required=False)
    data_first_available = serializers.DateField(
        format="%Y-%m-%d", input_formats=["%Y-%m-%d", "%d-%m-%Y"]
    )
    country_of_origin = serializers.ChoiceField(choices=CountryChoices.choices())
    packer = serializers.CharField(max_length=100)
    manufacturer = serializers.CharField(max_length=100)
    importer = serializers.CharField(max_length=100)
    gender = serializers.ChoiceField(choices=GenderChoices.choices())

    def validate_product(self, value):
        if value is None:
            raise serializers.ValidationError("Invalid product data")
        if hasattr(value, "is_deleted") or value.is_deleted:
            raise serializers.ValidationError("Product does not exist")
        return value

    def validate_dimension(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError(
                "Dimension value should be an integer value"
            )
        if value <= 0:
            raise serializers.ValidationError("Dimesion cannot be negative or zero")
        return value

    def validate_weight(self, value):
        if value and not isinstance(value, int):
            raise serializers.ValidationError("Weight value should be an integer value")
        if value < 0:
            raise serializers.ValidationError("Weight cannot be negative")
        return value

    def validate_data_first_available(self, value):
        if value is None:
            raise serializers.ValidationError("Invalid date value")
        if value > date.today():
            raise serializers.ValidationError("The date cannot be in the future")
        return value

    def validate_country_of_origin(self, value):
        if value is None:
            raise serializers.ValidationError("Invalid country of origin")
        if value not in CountryChoices.values():
            raise serializers.ValidationError("Country does not exist")
        return value

    def validate_packer(self, value):
        if value.strip() is None:
            raise serializers.ValidationError("Invalid packer value")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Packer name should only contain letters")
        return value

    def validate_manufacturer(self, value):
        if value.strip() is None:
            raise serializers.ValidationError("Invalid manufacturer value")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError(
                "Manufacturer name should only contain letters"
            )
        return value

    def validate_importer(self, value):
        if value.strip() is None:
            raise serializers.ValidationError("Invalid importer value")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError(
                "Importer name should only contain letters"
            )
        return value

    def validate_gender(self, value):
        if not value:
            raise serializers.ValidationError("Invalid gender value")
        if value not in GenderChoices.values():
            raise serializers.ValidationError("Gender Choice does not exist")
        return value


class ProductAttributeSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=ProductDetails.objects.all())
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    size = serializers.ChoiceField(choices=ProductSizeChoices.choices())

    def validate_product(self, value):
        if value is None:
            raise serializers.ValidationError("Invalid product data")
        if hasattr(value, "is_deleted") or value.is_deleted:
            raise serializers.ValidationError("Product does not exist")
        return value

    def validate_name(self, value):
        if value and not value.replace(" ", "").isalpha():
            raise serializers.ValidationError(
                "Product Attribute name should only contain letters"
            )
        return value

    def validate_color(self, value):
        if value.strip() is None:
            raise serializers.ValidationError("Invalid color value")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError(
                "Product attribute color should only contain letters"
            )
        return value

    def validate_size(self, value):
        if value is None:
            raise serializers.ValidationError("Invalid size of origin")
        if value not in ProductSizeChoices.values():
            raise serializers.ValidationError("Size does not exist")
        return value
