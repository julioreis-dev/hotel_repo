from rest_framework import viewsets, status
from rest_framework.views import APIView
from rooms.models import Hotels, Rooms, Reservation
from .serializers import HotelsSerializer, RoomsSerializer, ReservationsSerializer
from rest_framework.response import Response
from django.http import Http404


class HotelsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HotelsSerializer
    queryset = Hotels.objects.all()


class RoomsViewSet(APIView):
    serializer_class = RoomsSerializer

    def get(self, request, format=None):
        rooms = Rooms.objects.all()
        serializer = RoomsSerializer(rooms, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class ReservationViewSet(APIView):
    serializer_class = ReservationsSerializer

    def get(self, request, format=None):
        reservation = Reservation.objects.all()
        serializer = ReservationsSerializer(reservation, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
