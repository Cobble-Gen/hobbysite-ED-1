# Generated by Django 5.1.6 on 2025-05-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0007_alter_product_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=models.DecimalField(decimal_places=2, max_digits=10), max_digits=10, null=True),
        ),
    ]
