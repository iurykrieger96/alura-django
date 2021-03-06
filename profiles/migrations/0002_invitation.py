# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 01:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invited', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to='profiles.Profile')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_sent', to='profiles.Profile')),
            ],
        ),
    ]
