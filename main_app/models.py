from django.db import models
from datetime import datetime

class Event(models.Model):
    creation_date = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=250)
    event_start  = models.DateTimeField()
    participants = models.TextField()
    event_description = models.TextField()

class User(models.Model):
    creation_date = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=250)
    email_address = models.CharField(max_length=250)
    last_participation = models.DateTimeField()
