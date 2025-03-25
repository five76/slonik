import squares

# Чтение данных с клавиатуры, разделение их в список, поэлементное преобразование в целые числа
data = map(int,input('Введите данные ').split())
# Распаковка списка
a, b, c = data
print(squares.triangle(a,b,c))

print(squares.сircle(a))