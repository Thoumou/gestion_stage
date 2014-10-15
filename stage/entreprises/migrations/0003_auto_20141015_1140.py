# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0002_pays_villesdefrance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pays',
            old_name='alapha2',
            new_name='alpha2',
        ),
        migrations.RenameField(
            model_name='pays',
            old_name='alapha3',
            new_name='alpha3',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(null=True, max_length=75, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='entreprise',
            field=models.ForeignKey(to='entreprises.Entreprise', related_name='contacts'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='libelle',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nom',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]
