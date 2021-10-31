from django.db import models

# Create your models here.
class Component(models.Model):
    name = models.TextField(blank=True)
    cType = models.TextField(blank=True)
    value = models.TextField(blank=True)
    unit = models.TextField(blank=True)
    #token = models.TextField(blank=True)
    #id_user = models.TextField(blank=True)