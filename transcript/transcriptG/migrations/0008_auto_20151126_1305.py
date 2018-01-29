# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0007_auto_20151126_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='batchNo2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='batchNo2',
        ),
    ]
