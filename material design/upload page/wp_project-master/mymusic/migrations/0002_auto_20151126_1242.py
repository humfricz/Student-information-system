# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='mobilenumber',
            field=models.CharField(unique=True, max_length=15),
        ),
    ]
