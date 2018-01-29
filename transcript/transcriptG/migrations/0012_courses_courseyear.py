# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0011_studentmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='Courseyear',
            field=models.IntegerField(default=0),
        ),
    ]
