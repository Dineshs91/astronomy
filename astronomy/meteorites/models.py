from __future__ import unicode_literals

from django.db import models


class Meteorite(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    nametype = models.CharField(max_length=50)
    recclass = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    fall = models.CharField(max_length=50)
    year = models.DateTimeField()
    reclat = models.CharField(max_length=50)
    reclong = models.CharField(max_length=50)
    geolocation_address = models.CharField(max_length=50)
    geolocation_zip = models.CharField(max_length=50)
    geolocation_city = models.CharField(max_length=50)
    geolocation = models.CharField(max_length=50)
    geolocation_state = models.CharField(max_length=50)

    class Meta:
        db_table = 'meteorite'