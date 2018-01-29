# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=140)),
                ('lastname', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('mobilenumber', models.CharField(max_length=15)),
            ],
        ),
    ]
