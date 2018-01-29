# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0003_auto_20151124_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batchNo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='emailid',
            field=models.EmailField(max_length=400),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='yearofjoining',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='yearofpassing',
            field=models.IntegerField(default=0),
        ),
    ]
