# Generated by Django 5.1.6 on 2025-05-03 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0008_alter_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('O', 'Open'), ('F', 'Full')], default='O', max_length=255),
        ),
    ]
