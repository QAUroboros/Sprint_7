import pytest
from helpers import register_courier_and_return_password


@pytest.fixture(scope='session')
def courier():
    data = register_courier_and_return_password()
    yield data


@pytest.fixture
def courier_payload():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
