from django.db import models
from .common.choices import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.db.models.manager import Manager
from django.dispatch import receiver


class Institute(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)


class UserProfile(models.Model):
    Id = models.AutoField(primary_key=True)
    UserMain = models.OneToOneField(
        User, related_name='profile')
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    Institute = models.ForeignKey(Institute, on_delete=None)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(UserMain=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Patient(models.Model):
    Id = models.AutoField(primary_key=True)
    PID = models.IntegerField()
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Sex = models.IntegerField(choices=Sex, default=1)
    BirthDate = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=20)
    CatalogPath = models.CharField(max_length=30)
    CreationDate = models.DateTimeField()
    Doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def publish(self):
        self.save()


class Vist(models.Model):
    Id = models.AutoField(primary_key=True)
    Date = models.DateTimeField()
    CreateDate = models.DateTimeField()
    Details = models.CharField(max_length=300)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def publish(self):
        self.CreateDate = timezone.now
        self.save()


class Photography(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Directory = models.CharField(max_length=100)
    Discription = models.CharField(max_length=1000)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

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
