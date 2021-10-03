import json
from django.db import models
from datetime import datetime


class Wheater(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    date = models.CharField(max_length=20, default=str(datetime.now().date()))
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    temperatures = models.JSONField(null=False, blank=False)

    class Meta:
        verbose_name = 'Wheater'
        verbose_name_plural = 'Wheaters'
