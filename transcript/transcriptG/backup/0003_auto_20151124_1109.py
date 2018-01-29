# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0002_auto_20151124_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='batch',
            new_name='batchNo',
        ),
        migrations.AlterField(
            model_name='student',
            name='yearofjoining',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='yearofpassing',
            field=models.IntegerField(),
        ),
    ]
