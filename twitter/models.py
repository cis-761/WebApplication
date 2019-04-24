from django.db import models
from django.conf import settings
from django.utils import timezone

class Tweets(models.Model):
    text = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    favorite = models.BooleanField(default=False)
    date = models.DateTimeField

class ReTweets(models.Model):
    text = models.CharField(max_length=300) 

class User(models.Model):
    name = models.CharField(max_length=30)
    screen_name = models.CharField(max_length=30)
    geo_enabled = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

class Flu(models.Model):
    flu_type = models.CharField(max_length=30)

class Symptoms(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
