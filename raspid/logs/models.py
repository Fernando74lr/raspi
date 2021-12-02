from django.db import models
from django.conf import settings

# Create your models here.
class Log(models.Model):
    value = models.TextField(blank=True)
    name = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
