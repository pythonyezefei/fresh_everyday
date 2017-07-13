# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_auto_20170704_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='upasswd',
            field=models.CharField(max_length=100),
        ),
    ]
