#Екатерина Маматова, 22 кагорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data


def get_order_number(order_response):
    return order_response.json().get("track")

data.params_get["t"] = get_order_number(sender_stand_request.order_response)


#Проверка автотеста

def positive_assert():
    order_number_response = sender_stand_request.get_order_number(data.params_get)
    assert order_number_response.status_code == 200

def test_order_number():
    positive_assert()

print("Заказ создан. Трек номер:", data.params_get)

