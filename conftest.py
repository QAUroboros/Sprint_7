import pytest
from utils.helpers import register_courier_and_return_password


@pytest.fixture(scope='session')
def courier():
    data = register_courier_and_return_password()
    yield data
