import csv
from decimal import Decimal

def load_dataset(file_name=''):
    df = []
    #with open('bike_sales.csv', newline='',encoding='utf-8') as fp:
    with open(file_name, newline='',encoding='utf-8') as fp:    
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            df.append(row)
    return df


def define_sales_cities(city=None,bike=None,lst=[]):
    city_list = []
    #print(lst)
    for el in lst:
        city_list.append(el[6])
    return list(set(city_list))
    
    
def calculate_sum_city(city=None, lst=[]):
    
    df = list(filter(lambda x: x[6] == city, lst))
    sum = Decimal(0.0)
    for el in df:
        sum += Decimal(el[4]) * int(el[5])        
    return sum

if __name__ == '__main__':
    df = load_dataset(file_name='bike_sales_100k.csv')
    print(df[0])
    print(define_sales_cities(lst=df[:]))
    print(calculate_sum_city(city='Chicago',lst=df[:]))
    print(df[0])
