import pytest
import requests
import allure
from helpers import BASE_URL, generate_random_string


class TestOrders:


    @allure.title("Создание заказа")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_order(self,colors):
        payload = {
            "firstName" :generate_random_string(10),
            "lastName" :generate_random_string(10),
            "address" :generate_random_string(10),
            "metroStation" :4,
            "phone" : "+7 800 355 35 35",
            "rentTime" :5,
            "deliveryDate" :"2024-02-10",
            "comment" :"коммент",
            "color" : colors }

        response = requests.post(f'{BASE_URL}/orders', json=payload)
        assert response.status_code == 201
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"

    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        response = requests.get(f'{BASE_URL}/orders')
        assert response.status_code == 200
        assert "orders" in response.json(), "В ответе отсутствует поле 'orders'"