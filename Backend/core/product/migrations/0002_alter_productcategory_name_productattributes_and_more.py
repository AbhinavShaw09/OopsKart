# Generated by Django 5.1.3 on 2024-12-07 04:18

import datetime
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.IntegerField(choices=[(1, 'Sports'), (2, 'Electronics'), (3, 'Hardware'), (4, 'Kitchenanddining'), (5, 'Furniture'), (6, 'Homedecor'), (7, 'Lighting')], default=1),
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.IntegerField(choices=[(1, 'Xs'), (2, 'Sm'), (3, 'Md'), (4, 'Lg'), (5, 'Xl'), (6, 'Xxl')], default=4)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name_plural': 'ProductAttributes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('dimention', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('data_first_available', models.DateField(default=datetime.datetime.now)),
                ('country_of_origin', models.IntegerField(choices=[(1, 'India'), (2, 'Usa'), (3, 'Uk'), (4, 'Canada'), (5, 'Australia'), (6, 'Germany'), (7, 'France'), (8, 'Italy'), (9, 'Japan'), (10, 'China'), (11, 'Brazil'), (12, 'Southafrica'), (13, 'Russia'), (14, 'Mexico'), (15, 'Southkorea')], default=1)),
                ('packer', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('importer', models.CharField(max_length=100)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], default=1)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
