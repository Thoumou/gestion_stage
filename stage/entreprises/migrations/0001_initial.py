# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nom', models.CharField(max_length=100)),
                ('libelle', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('telephone', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=250)),
                ('codePostal', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=50)),
                ('pays', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=20)),
                ('latitude', models.DecimalField(max_digits=13, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=13, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='entreprise',
            field=models.ForeignKey(to='entreprises.Entreprise'),
            preserve_default=True,
        ),
    ]
