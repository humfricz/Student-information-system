# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0002_auto_20151126_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
