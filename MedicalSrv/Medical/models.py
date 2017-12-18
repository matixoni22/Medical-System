from django.db import models
from .common.choices import *
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.db.models.signals import post_save
from django.db.models.manager import Manager
from django.dispatch import receiver
import pathlib
import os


def GetUploadedPath(instance, filename):
    return '{0}/{1}'.format(instance.Visit.CatalogPath, filename)


class UserProfile(models.Model):
    Id = models.AutoField(primary_key=True)
    UserMain = models.OneToOneField(
        User, related_name='profile')
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(UserMain=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Patient(models.Model):
    Id = models.AutoField(primary_key=True)
    PID = models.IntegerField(unique=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Sex = models.IntegerField(choices=Sex, default=1)
    BirthDate = models.DateField()
    PhoneNumber = models.CharField(max_length=100)
    CatalogPath = models.CharField(max_length=100)
    CreationDate = models.DateTimeField()
    Doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def publish(self):
        self.CreationDate = datetime.now()
        catalogName = self.PID + '_' + self.LastName
        try:
            os.makedirs("Medical/medical_data/" + catalogName)
            self.CatalogPath = "Medical/medical_data/" + catalogName
        except OSError as init:
            print("error: ", init)
            raise EnvironmentError('Cannot add directory')
        self.save()


class Visit(models.Model):
    Id = models.AutoField(primary_key=True)
    Date = models.DateTimeField()
    CreateDate = models.DateTimeField()
    Details = models.CharField(max_length=300)
    CatalogPath = models.CharField(max_length=300)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def publish(self):
        self.CreateDate = datetime.now()
        try:
            directory = self.Patient.CatalogPath + "/" + str(self.Date)
            os.makedirs(directory)
            self.CatalogPath = directory
        except OSError as init:
            print("error: ", init)
            raise EnvironmentError('Cannot add directory')
        self.save()


class Result(models.Model):
    Id = models.AutoField(primary_key=True)
    Opaeration = models.CharField(max_length=200)
    Visit = models.OneToOneField(Visit, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='result_images/')

    def publish(self):
        self.save()


class Photography(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Discription = models.CharField(max_length=1000)
    Visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='images/')

    def publish(self):
        self.save()


class Disease(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=300)
    Photography = models.ForeignKey(Photography, on_delete=models.CASCADE)
    Discription = models.CharField(max_length=1000)

    def publish(self):
        self.save()


class Treatment(models.Model):
    Id = models.AutoField(primary_key=True)
    Disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    Descritpion = models.CharField(max_length=100)

    def publish(self):
        self.save()


class Medicine(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    AdministerOfDosages = models.CharField(max_length=100)
    Treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)

    def publish(self):
        self.save()
