from django.shortcuts import render
from rest_framework import viewsets

from meteorites.models import Meteorites
from meteorites.serializers import MeteoritesSerializer


class MeteoriteViewSet(viewsets.ModelViewSet):
    queryset = Meteorites.objects.all()
    serializer_class = MeteoritesSerializer