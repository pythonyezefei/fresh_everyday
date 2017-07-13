# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0006_auto_20170705_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='utel',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
