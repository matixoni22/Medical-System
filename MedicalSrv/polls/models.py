from django.db import models
from common.choices import *
from django.contrib.auth.models import User


class Institute(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)


class UserProfile(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.OneToOneField(User)
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
    Doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Photography(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Directory = models.CharField(max_length=100)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
