from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ParkingSlots, ParkingInteraction
from .parking_serializer import ParkingSerializer, ParkingInteractionSerializer

class IndexView(APIView):
    def get( self, request, format=None ):
        return Response("test")


class ListParking(APIView):

    def put( self, request, interaction_id=None):
        return Response({"message":"Thank for visit, see you soon."})


class ParkingViewSet(viewsets.ModelViewSet):
    queryset = ParkingSlots.objects.all()
    serializer_class = ParkingSerializer
    http_method_names = ['get', 'post', 'head', 'put']


class ParkingInteractionViewSet(viewsets.ModelViewSet):
    queryset = ParkingInteraction.objects.all()
    serializer_class = ParkingInteractionSerializer
    http_method_names = ['get', 'post', 'head']

