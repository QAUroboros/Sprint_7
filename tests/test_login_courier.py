import pytest
import requests
import allure
from helpers import BASE_URL, generate_random_string


class TestLoginCourier:

    @pytest.fixture(scope="class")
    def credentials_courier(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {"login": login, "password": password, "first_name": first_name}
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        assert response.status_code == 201
        return {"login": login, "password": password}

    @allure.title("Успешная авторизация курьера")
    def test_courier_login(self, credentials_courier):
        response = requests.post(f"{BASE_URL}/courier/login", json=credentials_courier)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация курьера с отсутствующими полями")
    def test_courier_without_fields(self):
        payload = {"login": generate_random_string(10)}
        response = requests.post(f"{BASE_URL}/courier/login", json=payload)
        assert response.status_code == 400

    @allure.title("авторизация с неверными данными ")
    def test_courier_login_invalid_data(self):
        payload = {"login": "invalid_login", "password": "invalid_password"}
        response = requests.post(f"{BASE_URL}/courier/login", json=payload)
        assert response.status_code == 404