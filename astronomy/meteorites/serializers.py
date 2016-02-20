from meteorites.models import Meteorite
from rest_framework import serializers


class MeteoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meteorite
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