# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0008_auto_20151126_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CID', models.CharField(max_length=10)),
                ('CName', models.CharField(max_length=15)),
                ('year', models.IntegerField(max_length=4)),
                ('term', models.IntegerField(max_length=1)),
                ('credits', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
        ),
    ]
