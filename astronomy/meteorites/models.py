from __future__ import unicode_literals

from django.db import models


class Meteorite(models.Model):
    name = models.TextField(max_length=50)
    id = models.IntegerField(primary_key=True)
    nametype = models.TextField(max_length=50)
    recclass = models.TextField(max_length=50)
    mass = models.FloatField()
    fall = models.TextField(max_length=50)
    year = models.DateTimeField()
    reclat = models.TextField(max_length=50)
    reclong = models.TextField(max_length=50)
    geolocation_address = models.TextField(max_length=50)
    geolocation_zip = models.TextField(max_length=50)
    geolocation_city = models.TextField(max_length=50)
    geolocation = models.TextField(max_length=50)
    geolocation_state = models.TextField(max_length=50)

    def __unicode__(self):
        return str(self.id) + " " + self.name