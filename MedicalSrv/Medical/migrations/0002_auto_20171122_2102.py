# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='FirstName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='LastName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='PhoneNumber',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='photography',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='FirstName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='LastName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Title',
            field=models.CharField(max_length=100),
        ),
    ]
