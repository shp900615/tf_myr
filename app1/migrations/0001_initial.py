# Generated by Django 5.0.6 on 2024-05-26 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='raw_crh_patient_diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_no', models.CharField(max_length=100)),
                ('clinic', models.CharField(max_length=100)),
                ('diagnosis_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('syc_month_year', models.CharField(max_length=10)),
                ('facility_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='raw_crh_patient_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_no', models.CharField(max_length=100)),
                ('bill_no', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=500)),
                ('amount', models.FloatField()),
                ('payment_category', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
                ('syc_month_year', models.CharField(max_length=10)),
                ('facility_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='raw_hrm_patient_dignosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_no', models.CharField(max_length=100)),
                ('clinic', models.CharField(max_length=100)),
                ('diagnosis_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('syc_month_year', models.CharField(max_length=10)),
                ('facility_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='raw_hrm_patient_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_no', models.CharField(max_length=100)),
                ('bill_no', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=500)),
                ('amount', models.FloatField()),
                ('payment_category', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
                ('syc_month_year', models.CharField(max_length=10)),
                ('facility_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FacilityToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
                ('facility', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.facilities')),
            ],
        ),
    ]
