# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('completed', models.BooleanField(default=False)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]