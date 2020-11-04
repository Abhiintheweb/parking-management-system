from rest_framework import serializers
from .models import ParkingSlots, ParkingInteraction


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlots
        fields = '__all__'


class ParkingInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingInteraction
        fields = '__all__'
