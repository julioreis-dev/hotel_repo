from rest_framework import serializers
from rooms.models import Hotels, Rooms, Reservation


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
