from django.db import models
from django.conf import settings
from django.utils import timezone

class Tweets(models.Model):
    text = models.CharField(max_length=5000, default='')
    location = models.CharField(max_length=5000, default='')
    favorite = models.BooleanField(default=False)
    date = models.CharField(max_length=5000, default='')
    rt = models.BooleanField(default=False)

class User(models.Model):
    name = models.CharField(max_length=5000)
    screen_name = models.CharField(max_length=5000)
    geo_enabled = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

class Flu(models.Model):
    flu_type = models.CharField(max_length=5000)

class Symptoms(models.Model):
    name = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)

class Trends(models.Model):
    trend = models.CharField(max_length=100)
    count = models.IntegerField

class fluSymptoms(models.Model):
    flu_id = models.ForeignKey(Flu, on_delete=models.CASCADE)
    symptoms_id = models.ForeignKey(Symptoms, on_delete=models.CASCADE)

class tweetFlu(models.Model):
    tweet_id = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    flu_id = models.ForeignKey(Flu, on_delete=models.CASCADE)

class userTweets(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_id = models.ForeignKey(Tweets, on_delete=models.CASCADE)

class tweetTrends(models.Model):
    tweet_id = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    trends_id = models.ForeignKey(Trends, on_delete=models.CASCADE)
