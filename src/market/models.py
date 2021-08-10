from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save


class MarketApk(models.Model):
    apk = models.CharField(max_length=300)
    title = models.CharField(max_length=300, null=True, blank=True)
    url = models.CharField(max_length=300, null=True, blank=True)
    descriptionHTML = models.CharField(max_length=10000, null=True, blank=True)
    summary = models.CharField(max_length=1000, null=True, blank=True)
    installs = models.CharField(max_length=100, null=True, blank=True)
    score = models.CharField(max_length=100, default='0', null=True, blank=True)
    ratings = models.CharField(max_length=100, null=True, blank=True)
    reviews = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    androidVersionText = models.CharField(max_length=100, null=True, blank=True)
    developer = models.CharField(max_length=200, null=True, blank=True)
    developerid = models.CharField(max_length=200, null=True, blank=True)
    developerEmail = models.CharField(max_length=100, null=True, blank=True)
    developerWebsite = models.CharField(max_length=300, null=True, blank=True)
    developerInternalID = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=300, null=True, blank=True)
    screenshots = models.JSONField(null=True, blank=True)
    contentRating = models.CharField(max_length=100, null=True, blank=True)
    released = models.CharField(max_length=100, null=True, blank=True)
    updated = models.CharField(max_length=100, null=True, blank=True)
    version = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_sync = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.apk


class ApkReview(models.Model):
    apk = models.ForeignKey(MarketApk, on_delete=models.CASCADE)
    userName = models.CharField(max_length=300, null=True, blank=True)
    userImage = models.CharField(max_length=300, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    score =models.IntegerField(null=True, blank=True)
    thumbsUpCount = models.IntegerField(null=True, blank=True)
    reviewCreatedVersion = models.CharField(max_length=1000, null=True, blank=True)
    at = models.DateTimeField(null=True, blank=True)
    replyContent = models.CharField(max_length=1000, null=True, blank=True)
    repliedAt = models.DateTimeField(null=True, blank=True)
    reviewId = models.CharField(max_length=1000, null=True, blank=True)
