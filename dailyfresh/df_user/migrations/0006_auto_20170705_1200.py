# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0005_auto_20170705_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddr',
            field=models.CharField(default=b'', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upasswd',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
