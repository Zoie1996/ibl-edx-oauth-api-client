# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 16:13
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OauthCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.TextField()),
                ('client_secret', models.TextField()),
                ('token_created_ts', models.DateTimeField(default=None, null=True)),
                ('expires_on', models.DateTimeField(default=None, null=True)),
                ('access_token', models.TextField(default='')),
            ],
        ),
    ]
