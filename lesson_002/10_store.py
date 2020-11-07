#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп
# ...

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
PRICE = 'price'
LAMP = 'Лампа'
TABLE = 'Стол'
SOFA = 'Диван'
CHAIR = 'Стул'
QUANTITY = 'quantity'

lamp_index = goods[LAMP]
lamps_quantity = store[lamp_index][0][QUANTITY]
lamps_cost = store[lamp_index][0][QUANTITY] * store[lamp_index][0][PRICE]
print(LAMP, '-', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_index = goods[TABLE]
table_quantity = store[table_index][0][QUANTITY] + store[table_index][1][QUANTITY]
table_cost = store[table_index][0][QUANTITY] * store[table_index][0][PRICE] +\
             store[table_index][1][QUANTITY] * store[table_index][1][PRICE]
print(TABLE, '-', table_quantity, 'шт, стоимость', table_cost, 'руб')

sofa_index = goods[SOFA]
sofa_quantity = store[sofa_index][0][QUANTITY]
sofa_cost = store[sofa_index][0][QUANTITY] * store[sofa_index][0][PRICE] + \
            store[sofa_index][1][QUANTITY] * store[sofa_index][1][PRICE]
print(SOFA, '-', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

chair_index = goods[CHAIR]
chair_quantity = store[chair_index][0][QUANTITY]
chair_cost = store[chair_index][0][QUANTITY] * store[chair_index][0][PRICE] + \
             store[chair_index][1][QUANTITY] * store[chair_index][1][PRICE] + \
             store[chair_index][2][QUANTITY] * store[chair_index][2][PRICE]
print(CHAIR, '-', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
print('===========================================================')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб
print(LAMP, '-', store[lamp_index][0][QUANTITY], 'шт, стоимость', store[lamp_index][0][PRICE], 'руб')
print(TABLE, '-', store[table_index][0][QUANTITY], 'шт, стоимость', store[table_index][0][PRICE], 'руб')
print(TABLE, '-', store[table_index][1][QUANTITY], 'шт, стоимость', store[table_index][1][PRICE], 'руб')
print(SOFA, '-', store[sofa_index][0][QUANTITY], 'шт, стоимость', store[sofa_index][0][PRICE], 'руб')
print(SOFA, '-', store[sofa_index][1][QUANTITY], 'шт, стоимость', store[sofa_index][1][PRICE], 'руб')
print(CHAIR, '-', store[chair_index][0][QUANTITY], 'шт, стоимость', store[chair_index][0][PRICE], 'руб')
print(CHAIR, '-', store[chair_index][1][QUANTITY], 'шт, стоимость', store[chair_index][1][PRICE], 'руб')
print(CHAIR, '-', store[chair_index][2][QUANTITY], 'шт, стоимость', store[chair_index][2][PRICE], 'руб')




##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






