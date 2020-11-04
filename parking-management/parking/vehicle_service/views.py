from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Vehicle
from .vehicle_serializer import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    http_method_names = ['get', 'post', 'head', 'put']
