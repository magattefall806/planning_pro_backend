# Generated by Django 5.1.1 on 2024-10-14 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('localisation', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'gestion_emploi_du_temps_departement',
            },
        ),
        migrations.CreateModel(
            name='Metier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_emploi_du_temps.departement')),
            ],
            options={
                'db_table': 'gestion_emploi_du_temps_metier',
            },
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nom', models.CharField(max_length=100)),
                ('date_debut', models.DateField(max_length=25)),
                ('date_fin', models.DateField(max_length=25)),
                ('metier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_emploi_du_temps.metier')),
            ],
            options={
                'db_table': 'gestion_emploi_du_temps_semestre',
            },
        ),
        migrations.CreateModel(
            name='UniteDEnseignement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
                ('volume_horaire', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_emploi_du_temps.semestre')),
            ],
            options={
                'db_table': 'gestion_emploi_du_temps_unitedenseignement',
            },
        ),
    ]
