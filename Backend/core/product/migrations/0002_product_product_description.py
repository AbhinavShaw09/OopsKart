# Generated by Django 5.1.3 on 2024-11-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
