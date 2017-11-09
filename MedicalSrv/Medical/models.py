from django.db import models
from .common.choices import *
from django.contrib.auth.models import User


class Institute(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)


class UserProfile(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.OneToOneField(User)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    Institute = models.ForeignKey(Institute, on_delete=None)


class Patient(models.Model):
    Id = models.AutoField(primary_key=True)
    PIN = models.IntegerField()
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Sex = models.IntegerField(choices=Sex, default=1)
    BirthDate = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=20)
    CatalogPath = models.CharField(max_length=30)
    CreationDate = models.DateTimeField()
    Doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Vist(models.Model):
    Id = models.AutoField(primary_key=True)
    Date = models.DateTimeField()
    CreteDate = models.DateTimeField()
    Details = models.CharField(max_length=300)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Photography(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Directory = models.CharField(max_length=100)
    Discription = models.CharField(max_length=1000)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Disease(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=300)
    Photography = models.ForeignKey(Photography, on_delete=models.CASCADE)
    Discription = models.CharField(max_length=1000)


class Treatment(models.Model):
    Id = models.AutoField(primary_key=True)
    Disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    Descritpion = models.CharField(max_length=100)


class Medicine(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    AdministerOfDosages = models.CharField(max_length=100)
    Treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
