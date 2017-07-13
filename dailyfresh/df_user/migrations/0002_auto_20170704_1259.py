# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddr',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upcode',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='utel',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
