# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0009_courses_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='credits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='courses',
            name='term',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='courses',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
