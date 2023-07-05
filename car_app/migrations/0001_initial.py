# Generated by Django 4.2.2 on 2023-07-04 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Model_Drive_Axle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Model_Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Model_Steering_Bridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Model_Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Model_Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service_Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_machine_no', models.CharField(max_length=255, unique=True)),
                ('head_engine_no', models.CharField(max_length=255)),
                ('head_transmission_no', models.CharField(max_length=255)),
                ('head_drive_axle_no', models.CharField(max_length=255)),
                ('head_steering_bridge_no', models.CharField(max_length=255)),
                ('deliver_contract_no', models.CharField(max_length=255)),
                ('date_shipment', models.DateField()),
                ('сonsignee', models.CharField(max_length=255)),
                ('delivery_address', models.CharField(max_length=255)),
                ('equipment', models.CharField(max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_client', to='car_app.client')),
                ('model_drive_axle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_drive_axle', to='car_app.model_drive_axle')),
                ('model_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_engine', to='car_app.model_engine')),
                ('model_steering_bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_steering_bridge', to='car_app.model_steering_bridge')),
                ('model_techique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_technique', to='car_app.model_technique')),
                ('model_transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_transmission', to='car_app.model_transmission')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_service_company', to='car_app.service_company')),
            ],
            options={
                'ordering': ['-date_shipment'],
            },
        ),
    ]
