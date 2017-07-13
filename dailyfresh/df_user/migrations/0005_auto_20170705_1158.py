# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0004_auto_20170705_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default=b'', max_length=20, null=True),
        ),
    ]
