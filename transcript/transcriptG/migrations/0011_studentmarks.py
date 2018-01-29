# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0010_auto_20151127_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SID', models.CharField(max_length=12)),
                ('CID', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=2)),
                ('description', models.CharField(default=b'null', max_length=50)),
            ],
        ),
    ]
