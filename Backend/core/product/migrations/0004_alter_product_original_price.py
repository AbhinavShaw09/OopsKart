# Generated by Django 5.1.3 on 2024-12-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
    ]