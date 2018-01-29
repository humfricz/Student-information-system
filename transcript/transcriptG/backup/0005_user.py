# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0004_auto_20151124_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
