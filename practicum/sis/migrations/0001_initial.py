# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('CID', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('CName', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=0)),
                ('term', models.IntegerField(default=0)),
                ('credits', models.IntegerField(default=0)),
                ('Courseyear', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('year', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('grade_string', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('SID', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('emailid', models.EmailField(max_length=400)),
                ('phnum', models.CharField(max_length=15)),
                ('yearofjoining', models.IntegerField(default=0)),
                ('yearofpassing', models.IntegerField(default=0)),
                ('batchNo', models.IntegerField(default=0)),
            ],
        ),
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
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
