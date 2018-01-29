# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0012_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hello',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
