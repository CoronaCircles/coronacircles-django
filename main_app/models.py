from django.db import models
from django.utils import timezone
import pytz

class Event(models.Model):
    name = models.CharField(max_length=150, unique=True)
    creation_date = models.DateTimeField(default=timezone.now)
    event_start  = models.DateTimeField()
    participants = models.TextField()
    event_description = models.TextField()


class User(models.Model):
    email_address = models.CharField(max_length=250)
