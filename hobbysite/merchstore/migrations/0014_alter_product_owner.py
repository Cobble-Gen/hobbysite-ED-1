# Generated by Django 5.1.6 on 2025-05-15 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0013_alter_product_merch_image'),
        ('user_management', '0004_alter_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='user_management.profile'),
        ),
    ]
