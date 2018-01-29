# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0004_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='language',
            field=models.CharField(default='english', unique=True, max_length=20),
            preserve_default=False,
        ),
    ]
