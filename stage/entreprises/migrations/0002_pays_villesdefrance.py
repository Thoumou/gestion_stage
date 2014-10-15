# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('code', models.PositiveSmallIntegerField(unique=True)),
                ('alapha2', models.CharField(max_length=2, unique=True)),
                ('alapha3', models.CharField(max_length=3, unique=True)),
                ('nom_en_gb', models.CharField(max_length=45)),
                ('nom_fr_fr', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VillesDeFrance',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='ville_id', serialize=False)),
                ('departement', models.CharField(max_length=3, db_column='ville_departement')),
                ('slug', models.CharField(max_length=255, db_column='ville_slug')),
                ('nom', models.CharField(max_length=45, db_column='ville_nom')),
                ('nom_reel', models.CharField(max_length=45, db_column='ville_nom_reel')),
                ('nom_soundex', models.CharField(max_length=45, db_column='ville_nom_soundex')),
                ('nom_metaphone', models.CharField(max_length=45, db_column='ville_nom_metaphone')),
                ('code_postal', models.CharField(max_length=255, db_column='ville_code_postal')),
                ('commune', models.CharField(max_length=3, db_column='ville_commune')),
                ('code_commune', models.CharField(max_length=5, db_column='ville_code_commune')),
                ('arrondissement', models.PositiveSmallIntegerField(db_column='ville_arrondissement')),
                ('canton', models.CharField(max_length=4, db_column='ville_canton')),
                ('amdi', models.PositiveSmallIntegerField(db_column='ville_amdi')),
                ('population_2010', models.PositiveIntegerField(db_column='ville_population_2010')),
                ('population_1999', models.PositiveIntegerField(db_column='ville_population_1999')),
                ('population_2012', models.PositiveIntegerField(db_column='ville_population_2012')),
                ('densite_2010', models.IntegerField(db_column='ville_densite_2010')),
                ('surface', models.PositiveIntegerField(db_column='ville_surface')),
                ('longitude_deg', models.FloatField(db_column='ville_longitude_deg')),
                ('latitude_deg', models.FloatField(db_column='ville_latitude_deg')),
                ('longitude_grd', models.CharField(max_length=9, db_column='ville_longitude_grd')),
                ('latitude_grd', models.CharField(max_length=8, db_column='ville_latitude_grd')),
                ('longitude_dms', models.CharField(max_length=9, db_column='ville_longitude_dms')),
                ('latitude_dms', models.CharField(max_length=8, db_column='ville_latitude_dms')),
                ('zmin', models.IntegerField(db_column='ville_zmin')),
                ('zmax', models.IntegerField(db_column='ville_zmax')),
                ('population_2010_order_france', models.IntegerField(db_column='ville_population_2010_order_france')),
                ('densite_2010_order_france', models.IntegerField(db_column='ville_densite_2010_order_france')),
                ('surface_order_france', models.IntegerField(db_column='ville_surface_order_france')),
            ],
            options={
                'db_table': 'villes_france',
            },
            bases=(models.Model,),
        ),
    ]
