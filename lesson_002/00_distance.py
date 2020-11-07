#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

X = 0
Y = 1

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# TODO здесь заполнение словаря
for root_city_name, root_city_value  in sites.items():
    distances[root_city_name] = {}
    for destination_city_name, destination_city_value  in sites.items():
        if root_city_name != destination_city_name:
            distance = ((root_city_value[X] - destination_city_value[X]) ** 2 +
                        (root_city_value[Y] - destination_city_value[Y]) ** 2 ) ** 0.5
            distances[root_city_name][destination_city_name] = distance

print(distances)




