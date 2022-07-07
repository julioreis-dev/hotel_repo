import pytest

pytestmark = pytest.mark.django_db


def test_hotels_info(setup_hotel):
    assert setup_hotel.name == 'transilvania'
    assert setup_hotel.address == 'street view'


def test_hotel_home(setup_hotel, client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.template_name[0] == 'home/index.html'
    assert 'home/index.html' in response.template_name


def test_hotel_without_login(setup_hotel, client):
    response = client.get('/hotels/')
    assert response.status_code == 302


def test_hotel_room_without_login(setup_hotel, client):
    response = client.get(f'/hotel/rooms/{setup_hotel.pk}/')
    assert response.status_code == 302


def test_room_info(setup_room):
    assert setup_room.number == 101
    assert setup_room.price == 35.00
    assert setup_room.active == True


def test_login_url(client):
    response = client.get('/accounts/login/')
    assert response.status_code == 200
    assert 'account/login.html' in response.template_name
