import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(scope='function')
def customuser():
    User = get_user_model()
    return User

