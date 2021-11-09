from django.db import models
from django.conf import settings

# Create your models here.
class Component(models.Model):
    name = models.TextField(blank=True)
    cType = models.TextField(blank=True)
    value = models.TextField(blank=True)
    unit = models.TextField(blank=True)
    #token = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
