from django.db import models
from common.choices import *


class Institute(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)


class User(models.Model):
    Id = models.AutoField(primary_key=True)
    Login = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Email = models.EmailField()
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Institute = models.ForeignKey(Institute, on_delete=None)


class Patient(models.Model):
    Id = models.AutoField(primary_key=True)
    PIN = models.IntegerField()
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Sex = models.IntegerField(choices=Sex, default=1)
    BirthDate = models.DateTimeField()
    CatalogPath = models.CharField(max_length=30)
    CreationDate = models.DateTimeField()
    Doctor = models.ForeignKey(User, on_delete=models.CASCADE)


class Photography(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Directory = models.CharField(max_length=100)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
