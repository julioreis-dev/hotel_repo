import pytest
from ..models import Hotels, Rooms
from users.models import User


@pytest.fixture(scope='function')
def setup_hotel():
    return Hotels.objects.create(name='transilvania', address='street view')


@pytest.fixture(scope='function')
def setup_room():
    hotel = Hotels.objects.create(name='transilvania', address='street view')
    return Rooms.objects.create(number=101, price=35.00, hotels=hotel)

