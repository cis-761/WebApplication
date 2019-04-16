from django.db import models
from django.conf import settings
from django.utils import timezone

class Tweets(models.Model):
    # id - implicit, not null, primary key
    text = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    favorite = models.BooleanField(default=False)
    date = models.DateTimeField

class ReTweets(models.Model):
     # id - implicit, not null, primary key
      text = models.CharField(max_length=300) # double check what the current character count limit for tweets are 

class User(models.Model):
     # id - implicit, not null, primary key
     name = models.CharField(max_length=30)
     screen_name = models.CharField(max_length=30)
     geo_enabled = models.BooleanField(default=False)
     verified = models.BooleanField(default=False)
     
