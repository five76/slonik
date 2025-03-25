import csv

def define_city_sales(lst=[]):
    """
    Города продаж
    """
    city_list = []
    for el in lst:
        city_list.append(el[6])
    city_list = list(set(city_list))
    return city_list

def calculate_sum_city(city=None, lst=[]):
    """
    Сумма продаж в городе
    """
    money = 0
    for el in lst:
        if el[6] == city:
            money += float(el[4]) * float(el[5])
    return money

def sum_bike_model(model, lst=[]):
    """
    Стоимость проданных велосипедов определенной модели
    """
    sum = 0
    for el in lst:
        if el[3] == model:
            sum += float(el[4]) * int(el[5])

    return sum

def define_bike_model(lst=[]):
    """
    Модели велосипедов
    """
    model_list = []
    for el in lst:
        model_list.append(el[3])
    model_list = list(set(model_list))
    return model_list