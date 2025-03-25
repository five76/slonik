import math

def triangle(*args):
        """
        Вычисление площади треугольника
        """

        # Если передано три аргумента, то рассчитать по формуле Герона
        if len(args) == 3:
                a, b, c = args
                p = (a + b + c) / 2
                s = math.sqrt(p * (p - a) * (p - b) * (p - c))
                return s
        # иначе если передано 2 аргумента, то рассчитать по формуле "половина основания на высоту"
        elif len(args) == 2:
                 a, b = args
                 return 1 / 2 * a * b
        # Иначе вывести предупреждение
        else:
                print('Некорректный ввод данных')

def  сircle(r):
        """
        Вычисление площади круга
        """

        return math.pi * r * r


if __name__ == '__main__':
        data = map(int,input('Введите данные ').split())
        # Распаковка списка
        a, b = data

        print(triangle(a,b))