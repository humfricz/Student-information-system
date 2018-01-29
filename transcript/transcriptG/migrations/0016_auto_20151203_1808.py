# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0015_remove_user_hello'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='CName',
            field=models.CharField(max_length=50),
        ),
    ]
