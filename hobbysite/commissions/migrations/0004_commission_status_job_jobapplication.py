# Generated by Django 5.1.6 on 2025-05-03 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0003_alter_commission_options'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='status',
            field=models.CharField(choices=[('O', 'Open'), ('F', 'Full'), ('C', 'Complete'), ('D', 'Discontinued')], default='O', max_length=255),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('manpowerRequired', models.IntegerField()),
                ('status', models.CharField(choices=[('O', 'Open'), ('F', 'Full')], default='O', max_length=255)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True)),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='commissions.commission')),
            ],
            options={
                'ordering': ['-UpdatedOn'],
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')], default='P', max_length=255)),
                ('AppliedOn', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobApplication', to='user_management.profile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobApplication', to='commissions.commission')),
            ],
            options={
                'ordering': ['-AppliedOn'],
            },
        ),
    ]
