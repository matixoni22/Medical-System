# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('PIN', models.IntegerField()),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Sex', models.IntegerField(choices=[(1, 'Female'), (2, 'Male')], default=1)),
                ('BirthDate', models.DateTimeField()),
                ('CatalogPath', models.CharField(max_length=30)),
                ('CreationDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Directory', models.CharField(max_length=100)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Login', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Institute')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='Doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.User'),
        ),
    ]
