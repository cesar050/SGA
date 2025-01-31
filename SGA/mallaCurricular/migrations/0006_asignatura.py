# Generated by Django 5.0.6 on 2024-05-30 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallaCurricular', '0005_alter_ciclo_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
                ('aa', models.CharField(max_length=10)),
                ('acd', models.CharField(max_length=10)),
                ('ape', models.CharField(max_length=10)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaturasList', to='mallaCurricular.ciclo')),
            ],
        ),
    ]
