from meteorites.models import Meteorites
from rest_framework import serializers


class MeteoritesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meteorites
        fields = (
            'id',
            'name',
            'nametype',
            'recclass',
            'mass',
            'fall',
            'year',
            'reclat',
            'reclong',
            'geolocation_address',
            'geolocation_zip',
            'geolocation_city',
            'geolocation',
            'geolocation_state'
        )