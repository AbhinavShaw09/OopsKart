# Generated by Django 5.1.3 on 2024-11-20 02:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.IntegerField(choices=[(1, 'SPORTS'), (2, 'ELECTRONICS'), (3, 'HARDWARE'), (4, 'KITCHEN_AND_DINING'), (5, 'FURNITURE'), (6, 'HOME_DECOR'), (7, 'LIGHTING')], default=1)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('in_stock', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('in_stock', models.BooleanField(default=True)),
                ('review_average_rating', models.FloatField(null=True)),
                ('review_count', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
    ]
