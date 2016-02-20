from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from meteorites.models import Meteorite
from meteorites.serializers import MeteoriteSerializer


class MeteoriteViewSet(viewsets.ModelViewSet):
    queryset = Meteorite.objects.all().order_by('id')
    serializer_class = MeteoriteSerializer