# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptG', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
