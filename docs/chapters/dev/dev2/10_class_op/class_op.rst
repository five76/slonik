Классы операторов
#################

Методы доступа
**************

.. figure:: img/10_01_metod.png
       :scale: 100 %
       :align: center
       :alt: asda


ПРАКТИКА
========

**Методы доступа**

::

	CREATE DATABASE ext_opclasses;

	CREATE DATABASE

::

	\c ext_opclasses

	You are now connected to database "ext_opclasses" as user "student".

В версии 16 имеется единственный встроенный табличный метод доступа:

::

	SELECT amname FROM pg_am WHERE amtype = 't';

	 amname 
	--------
	 heap
	(1 row)

Зато много различных индексных методов доступа:

::

	SELECT amname FROM pg_am WHERE amtype = 'i';

	 amname 
	--------
	 btree
	 hash
	 gist
	 gin
	 spgist
	 brin
	(6 rows)

**btree** — это «обычный» метод доступа на основе B-дерева, который используется по умолчанию и покрывает большинство потребностей. Остальные методы доступа также очень полезны, но в специальных ситуациях. Некоторые из них мы рассмотрим позже.

Для получения информации мы делали запросы к таблицам системного каталога, однако в арсенале psql есть удобная команда, позволяющая получить информацию о методах доступа, классах и семействах операторов, ей дальше мы и будем пользоваться:

::

	\dA

	List of access methods
	  Name  | Type  
	--------+-------
	 brin   | Index
	 btree  | Index
	 gin    | Index
	 gist   | Index
	 hash   | Index
	 heap   | Table
	 spgist | Index
	(7 rows)