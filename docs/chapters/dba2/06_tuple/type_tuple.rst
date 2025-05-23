Кортежи
~~~~~~

Кортежи (**tuple**) — это неизменяемый тип данных в Python, который используется для хранения упорядоченной последовательности элементов.

Кортежи представляют собой простые группы объектов. Они действуют точно так же, как списки, за исключением того, что не допускают непосредственного изменения (они являются неизменяемыми) и в литеральной форме записываются как последовательность элементов в **круглых**, а не в квадратных скобках.

Так как кортежей являются неизменяемыми коллекциями, то они обеспечивают поддержку целостности. Кортеж не будет изменен посредством другой ссылки из другого места в программе, чего нельзя сказать о списках. Существуют ситуации, в которых кортежи можно использовать, а списки – нет. Например, в качестве ключей словаря. Некоторые встроенные операции также могут требовать или предполагать использование кортежей, а не списков. 

.. important:: Списки должны выбираться, когда требуются упорядоченные коллекции, которые можно изменить. Кортежи могут использоваться в остальных случаях, когда необходимы фиксированные ассоциации объектов.

Кортеж поддерживают практически все операции над списками.

**Примеры кортежей**

.. code:: Python

        # Кортеж из строк
        fruits_tuple = ('яблоко', 'банан', 'апельсин')

        # Кортеж из логических значений
        my_tuple = (True, False, True)

        # Кортеж из других кортежей
        nested_tuple = ((1, 3), ('a', 'b'))

        # Кортеж из списков
        my_tuple = ([1, 2, 3], ['a', 'b', 'c'])

        # Кортеж из словарей
        my_tuple = ({'name': 'Mike', 'age': 18}, {'name': 'Anna', 'age': 21})

        # Кортеж из разных типов данных
        mixed_tuple = (1, 'hello', [1, 2, 3], {'a': 10})

Создание кортежей
``````````````````

- С помощью скобок:

fruits_tuple = ('яблоко', 'банан', 'апельсин')

- C помощью перечисления:

fruits_tuple = 'яблоко', 'банан', 'апельсин'

- Из итерируемого элемента с помощью функции tuple():

my_tuple_string = tuple('Jupyter')

my_tuple_list = tuple([1,2,3,4])

- Пустой кортеж:

empty_tuple = ()

Доступ к элементам
```````````````````````

Кортеж — это упорядоченная последовательность, поэтому для доступа к его элементам можно использовать индексы.

Индексация начинается с нуля. ПОследний индекс - значение, равное длине кортежа, уменьшенное на единицу.


.. code:: python

        fruits_tuple = ('яблоко', 'банан', 'апельсин')
        print(fruits_tuple[0])

        яблоко

Срезы
```````````````````````
.. code:: python

        fruits_tuple = ('яблоко', 'банан', 'апельсин', 'киви', 'абрикос')
        print(fruits_tuple[1:3])

        ('банан', 'апельсин')

Распаковка кортежа. 
````````````````````

Элементы кортежа извлекаются в переменные:

.. code:: python

	a, b, c, d = my_tuple
	# Теперь переменные a, b, c, d содержат значения из кортежа
	# a = 1, b = 2, c = 3, d = 'hello'

Обмен значениями между переменными
`````````````````````````````````````

.. code:: python

	x = 5
	y = 10
	# Обмен значениями с использованием кортежа, упаковки и распаковки
	x, y = y, x
	# x и y содержат новые значения
	print('x =', x) # Вывод: x = 10
	print('y =', y) # Вывод: y = 10
	
1. Операция упаковки (y, x)  создаёт кортеж из двух значений (10, 5), 
2. Операция распаковки (x, y) распаковывает кортеж и присваивает значения переменным x и y соответственно. Теперь переменная x = 10, а y = 5.

Конкатенация. 
``````````````

Это объединение двух кортежей в один новый кортеж с помощью оператора **+**

.. code:: python

	tup_1 = (1, 2, 3)
	tup_2 = (4, 5, 6)
	tup3 = tup_1 + tup_2
	print(f'Конкатенация кортежей {tup_3}')

	Конкатенация кортежей: (1, 2, 3, 4, 5, 6)

Преобразование в другие типы данных
````````````````````````````````````

**Преобразование кортежа в список**

.. code:: python
	
	my_tuple = (1, 2, 3, 4, 5)
	# Преобразование кортежа в список
	my_list = list(my_tuple)
	
	print('Кортеж:', my_tuple)
	print('Список:', my_list)
	
	Кортеж: (1, 2, 3, 4, 5)
	Список: [1, 2, 3, 4, 5]
	
	
**Преобразование кортежа в строку**

.. code:: python

	my_tuple = ('я','б','л','о','к','о')


	# Преобразование кортежа в строку
	my_string = ''.join(map(str, my_tuple))


	print('Кортеж:' my_tuple)
	print('Строка:', my_string)

	Кортеж: ('я','б','л','о','к','о')
	Строка: яблоко
	
	
Преобразование кортежа во множество
```````````````````````````````````

.. code:: python

	my_tuple = (1, 2, 3, 2, 4, 3, 4)



	# Преобразование кортежа во множество, при котором удаляются повторяющиеся элементы
	my_set = set(my_tuple)

	print('Кортеж:', my_tuple)
	print('Множество:', my_set)

	Кортеж: (1, 2, 3, 2, 4, 3, 4)
	Множество: {1, 2, 3, 4}

Множества — это неупорядоченные коллекции, которые состоят из уникальных элементов. 
В процессе преобразования последовательностей во множество все дубликаты в нём удаляются.

Преобразование кортежа в словарь
`````````````````````````````````

Кортеж в словарь (пары «ключ — значение»):

.. code:: python


	my_tuple = (('a', 1), ('b', 2), ('c', 3))

	# Преобразование кортежа в словарь
	my_dict = dict(my_tuple)

	print('Кортеж:', my_tuple)
	print('Словарь:', my_dict)

	Кортеж: (('a', 1), ('b', 2), ('c', 3))
	Словарь: {'a': 1, 'b': 2, 'c': 3}

Изменение кортежа
```````````````````

Кортеж является неизменяемой последовательностью, поэтому изменить его непосредственно нельзя.

Агоритм изменения:

- Кортеж преобразовать в список;
- Изменить список;
- Список преобразовать обратно в кортеж.

.. code:: python
	
	# Добавить 7 в кортеж (1, 2, 3, 4, 5)
	
	my_tuple = (1, 2, 3, 4, 5)
	
	# Преобразование кортежа в список
	my_list = list(my_tuple)
	print('Исходный кортеж:', my_tuple)
	print('ID: ', id(my_tuple))
	
	# Изменение списка
	my_list.append(7)
	
	# Преобразование списка в кортеж
	my_tuple = tuple(my_list)
	
	print('Имененный кортеж:', my_tuple)
	print('ID: ', id(my_tuple))
	
	Исходный кортеж: (1, 2, 3, 4, 5)
	ID:  2302337692224
	Имененный кортеж: (1, 2, 3, 4, 5, 7)
	ID:  2302337616480

Удаление кортежа
```````````````````

.. code:: python
	
	del my_tuple

Опредление длины, минимального, максимального элемента кортежа выполняется как в списках.