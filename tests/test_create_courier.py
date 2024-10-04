import allure
import requests
from helpers import BASE_URL, generate_random_string


class TestCreateCourier:

    @allure.title("Создание курьера успешно")
    def test_create_courier(self, courier_payload):
        response = requests.post(f"{BASE_URL}/courier", json=courier_payload)
        assert response.status_code == 201
        assert response.json()["ok"] == True

    @allure.title("Создание курьера дубликат")
    def test_create_dublicate_courier(self, courier_payload):
        response = requests.post(f"{BASE_URL}/courier", json=courier_payload)
        assert response.status_code == 201
        dublicate_response = requests.post(f"{BASE_URL}/courier", json=courier_payload)
        assert dublicate_response.status_code == 409

    @allure.title("создание курьера с отсутствующими полями")
    def test_create_courier_without_fields(self):
        payload_without_login = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(f"{BASE_URL}/courier", json=payload_without_login)
        assert response.status_code == 400

        payload_without_login_and_password = {
            "firstName": generate_random_string(10)
        }

        response_without_fields = requests.post(f"{BASE_URL}/courier", json=payload_without_login_and_password)
        assert response_without_fields.status_code == 400

    @allure.title("Создание курьера с существующим логином")
    def test_user_with_a_login_that_already_exists(self,courier_payload):
        response = requests.post(f"{BASE_URL}/courier", json=courier_payload)
        assert response.status_code == 201
        dublicate_response = requests.post(f"{BASE_URL}/courier", json=courier_payload)
        assert dublicate_response.status_code == 409
        expected_error_message = "Этот логин уже используется"
        assert dublicate_response.json()["message"] == expected_error_message
