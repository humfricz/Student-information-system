# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0006_auto_20151125_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batchNo2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='batchNo2',
            field=models.IntegerField(default=0),
        ),
    ]
