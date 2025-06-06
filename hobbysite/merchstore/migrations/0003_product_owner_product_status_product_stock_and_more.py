# Generated by Django 5.1.6 on 2025-04-17 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0002_product'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('AVL', 'Available'), ('SALE', 'On Sale'), ('OOS', 'Out of Stock')], default='AVL', max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('CART', 'On Cart'), ('PAY', 'To Pay'), ('SHIP', 'To Ship'), ('RECEIVE', 'To Receive'), ('DELIVERED', 'Delivered')], max_length=15)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='user_management.profile')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='merchstore.product')),
            ],
        ),
    ]
