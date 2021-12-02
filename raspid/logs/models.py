from django.db import models
from django.conf import settings

# Create your models here.
class Log(models.Model):
    value = models.TextField(blank=True)
    component = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
