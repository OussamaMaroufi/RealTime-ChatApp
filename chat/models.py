from django.db import models
from django.contrib.auth.models import User



class Room(models.Model):
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=User, blank=True)

