# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mymusic.models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0003_admins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail', models.FileField(upload_to=mymusic.models.get_upload_file_name)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
            ],
        ),
    ]
