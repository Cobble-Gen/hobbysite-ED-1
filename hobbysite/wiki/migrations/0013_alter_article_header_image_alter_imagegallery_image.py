# Generated by Django 5.1.6 on 2025-05-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0012_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='header_image',
            field=models.ImageField(null=True, upload_to='images/wiki/'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='image',
            field=models.ImageField(upload_to='images/wiki/'),
        ),
    ]
