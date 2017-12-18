# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-17 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Medical', '0004_photography_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Opaeration', models.CharField(max_length=200)),
                ('Image', models.ImageField(upload_to='images/')),
                ('Visit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Medical.Visit')),
            ],
        ),
        migrations.AlterField(
            model_name='photography',
            name='Image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
