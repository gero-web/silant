# Generated by Django 4.2.2 on 2023-06-30 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kind_Technique_Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization_Tat_Carried_Out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Technique_Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_holding_TO', models.DateField()),
                ('operating_time_mh', models.PositiveIntegerField()),
                ('dress_order_no', models.CharField()),
                ('dress_order', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TO_Car', to='car_app.car')),
                ('kind_technique_maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kind_TO', to='technique_maintenance_app.kind_technique_maintenance')),
                ('organization_that_carried_TO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TO_organization_that_carried', to='technique_maintenance_app.organization_tat_carried_out')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technique_maintenance_service_company', to='car_app.service_company')),
            ],
        ),
    ]