# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0006_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlaylist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('songName', models.ForeignKey(to='mymusic.Songs')),
                ('user', models.ForeignKey(to='mymusic.Userdetails')),
            ],
        ),
    ]
