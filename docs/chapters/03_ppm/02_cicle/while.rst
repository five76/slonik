Цикл while
~~~~~~~~~~~

Очень часто одно и то же действие надо выполнить для набора однотипных данных. Например, преобразовать все строки в списке в верхний регистр. Для выполнения таких действий в Python используется цикл for.

Цикл while используется в случаях, когда количество итераций цикла неопределено (при неправильном подходе может оказаться и бесконечным)

Синтаксис:

.. code:: python

	while <условие>:
		тело цикла

Печатать значения, пока их значения меньше 6

.. code:: python

	i = 1
	while i < 6:
	  print(i)
	  i += 1
	i = 1
	while i < 6:
	  print(i)
	  i += 1

	1
	2
	3
	4
	5

Заполнять с клавиатуры список строками, пока не будет введена пустая строка

.. code:: python

	my_list = []
	input_string = input('Введите строку:')
	while input_string:
		my_list.append(input_string)
		input_string = input('Введите строку:')
	print(my_list)
	my_list = []
	input_string = input('Введите строку:')
	while input_string:
		my_list.append(input_string)
		input_string = input('Введите строку:')
	print(my_list)

	Введите строку:Visual Studio Code
	Введите строку:PyCharm
	Введите строку:Jupyter Notebook
	Введите строку:
	['Visual Studio Code', 'PyCharm', 'Jupyter Notebook']


2 способ:

.. code:: python

	my_list = []
	while True:
		# Запрос и чтение строки
		input_string = input('Введите строку:')
		# Если введена пустая строка, то input_string - это False 
		# => not input_string - это True
		if not input_string:
			break
		my_list.append(input_string)
		
	print(my_list)

	Введите строку:Роза
	Введите строку:Астра
	Введите строку:
	['Роза', 'Астра']

Операции continue, break, else применяются аналогично for