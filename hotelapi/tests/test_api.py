import json
import pytest
from django.urls import reverse
from rooms.models import Hotels, Rooms, Reservation
from users.models import User

hotels_url = reverse("api:hotelsview-list")
room_url = reverse("api:rooms")
reservation_url = reverse("api:reservations")
pytestmark = pytest.mark.django_db


def test_zero_hotel_should_return_empty_list(client) -> None:
    response = client.get(hotels_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_hotel_exist_should_succeed(client):
    Hotels.objects.create(name='transilvania', address='street view')
    response = client.get(hotels_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content['name'] == 'transilvania'
    assert response_content['address'] == 'street view'


def test_one_room_exist_should_succeed(client):
    hotels = Hotels.objects.create(name='transilvania', address='street view')
    Rooms.objects.create(number=101, price=35.00, hotels=hotels)
    response = client.get(room_url)
    response_content = json.loads(response.content)['data'][0]
    assert response.status_code == 200
    assert response_content['number'] == 101
    assert response_content['price'] == '35.00'
    assert response_content['hotels'] == hotels.pk


def test_one_reservation_exist_should_succeed(client):
    user = User.objects.create(username='will', email='will@email.com', password='testpass123')
    hotels = Hotels.objects.create(name='transilvania', address='street view')
    room = Rooms.objects.create(number=101, price=35.00, hotels=hotels)
    Reservation.objects.create(client_user=user, checkin= '2022-07-09 00:00:00', number_host=0, rooms=room)
    response = client.get(reservation_url)
    response_content = json.loads(response.content)['data'][0]
    assert response.status_code == 200
    assert response_content['client_user'] == user.id
    assert response_content['number_host'] == 0
    assert response_content['rooms'] == room.id
