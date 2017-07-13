# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upasswd', models.CharField(max_length=20)),
                ('uemail', models.EmailField(max_length=254)),
                ('utel', models.IntegerField()),
                ('uaddr', models.CharField(max_length=100)),
                ('upcode', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
