# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0003_auto_20170704_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uaddr',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
