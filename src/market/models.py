from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.query import InstanceCheckMeta
from django.db.models.signals import post_save



class MarketApk(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    apk = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    last_sync = models.DateTimeField(null=True, blank=True)
    installs = models.CharField(max_length=100, null=True, blank=True)
    score = models.CharField(max_length=100, default='0', null=True, blank=True)
    ratings = models.CharField(max_length=100, null=True, blank=True)
    reviews = models.CharField(max_length=100, null=True, blank=True)
    developer = models.CharField(max_length=200, null=True, blank=True)
    developerid = models.CharField(max_length=200, null=True, blank=True)
    developerEmail = models.CharField(max_length=100, null=True, blank=True)
    developerWebsite = models.CharField(max_length=300, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    contentRating = models.CharField(max_length=100, null=True, blank=True)
    released = models.CharField(max_length=100, null=True, blank=True)
    updated = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.apk

class Developer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    developerid = models.CharField(max_length=200, null=True, blank=True)
    apps = models.IntegerField(blank=True, null=True)
