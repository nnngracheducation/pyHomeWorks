#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
# sweets = {
#     'название сладости': [
#         {'shop': 'название магазина', 'price': 99.99},
#         # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
#     ],
#     # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
# }
# Указать надо только по 2 магазина с минимальными ценами


BEST_POSITIONS_TO_SHOW_COUNT = 2
NAME_INDEX = 0
PRICE_INDEX = 1

products = {}
for shop_name, shop_data in shops.items():
    for product_data in shop_data:
        if product_data['name'] not in products:
            products[product_data['name']] = {}
        if shop_name not in products[product_data['name']]:
            products[product_data['name']][shop_name] = {}

        products[product_data['name']][shop_name] = product_data['price']


filtered_products = {}
for product_name, product_prices in products.items():
    dict_as_list = product_prices.items()
    sorted_list = sorted(dict_as_list, key=lambda x: x[PRICE_INDEX])
    low_trim_index = -1 * BEST_POSITIONS_TO_SHOW_COUNT
    filtered_list = sorted_list[low_trim_index:]

    filtered_product_data = {}
    for filtered_product in filtered_list:
        filtered_product_data[filtered_product[NAME_INDEX]] = filtered_product[PRICE_INDEX]

    filtered_products[product_name] = filtered_product_data


print(filtered_products)