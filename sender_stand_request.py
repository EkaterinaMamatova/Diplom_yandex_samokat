#Екатерина Маматова, 22 кагорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

#Запрос на создание заказа

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

order_response = post_new_order(data.order_body)

#Запрос на получения заказа по треку заказа

def get_order_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_NUMBER,
                        params=track_number)