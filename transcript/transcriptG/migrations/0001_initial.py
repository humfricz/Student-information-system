# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SID', models.CharField(max_length=12)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('emailid', models.EmailField(max_length=20)),
                ('phnum', models.CharField(max_length=15)),
                ('yearofjoining', models.IntegerField(max_length=4)),
                ('yearofpassing', models.IntegerField(max_length=4)),
                ('batch', models.IntegerField(max_length=1)),
            ],
        ),
    ]
