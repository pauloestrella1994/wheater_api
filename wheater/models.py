from django.db import models
from datetime import datetime


class Wheater(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    date = models.CharField(max_length=20, default=str(datetime.now().date()))
    lat = models.DecimalField(max_digits=6, decimal_places=4)
    lon = models.DecimalField(max_digits=6, decimal_places=4)
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    temperatures = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = 'Wheater'
        verbose_name_plural = 'Wheaters'
