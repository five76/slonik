Мониторинг
##########

Средства опреационной системы
*****************************

.. figure:: img/monitor_01.png
       :scale: 100 %
       :align: center
       :alt: asda
	   
PostgreSQL работает под управлением операционной системы ив известной степени зависит от ее настроек.

Используя инструменты операционной системы, можно посмотреть информацию о процессах PostgreSQL. При включенном (по умолчанию) параметре сервера **update_process_title** 
в имени процесса отображается его текущее состояние. Параметр **cluster_name** задает имя экземпляра, по которому его можно отличать в списке процессов.

Для изучения использования системных ресурсов (процессор, память, диски) в Unix имеются различные инструменты: iostat, vmstat, sar, topи др.

Необходимо следить и за размером дискового пространства. Место, занимаемое базой данных, можно смотреть как из самой БД, так из ОС (команда du). 
Размер доступного дискового пространства надо смотреть в ОС (команда df). Если используются дисковые квоты, надо принимать во внимание и их.

В целом набор инструментов и подходы могут сильно различаться в зависимости от используемой ОС и файловой системы.

https://postgrespro.ru/docs/postgresql/16/monitoring-ps

https://postgrespro.ru/docs/postgresql/16/diskusage

Статистика
**********

Существует два основных источника информации о происходящемв системе:

- Cтатистическая информация, которая собирается PostgreSQL и хранится в кластере.

- Журнал сообщений.

Сбор статистики
===============

.. figure:: img/monitor_02.png
       :scale: 100 %
       :align: center
       :alt: asda

Система накопительной статистики в PostgreSQL собирает и позволяет получать информацию о работе сервера. Накопительная статистика отслеживает обращения к таблицам и 
индексам как на уровне блоков на диске, так и на уровне отдельных строк. Кроме того, для каждой таблицы собираются сведения о количестве строк и действиях по очистке и анализу.

Можно также учитывать количество вызовов пользовательских функций и время, затраченное на их выполнение.

Количеством собираемой информации управляют несколько параметров сервера, так как чем больше информации собирается, тем больше и накладные расходы.

https://postgrespro.ru/docs/postgresql/16/monitoring-stats

Архитектура
===========

.. figure:: img/monitor_03.png
       :scale: 100 %
       :align: center
       :alt: asda
	   
Обслуживающие процессы собирают статистику в рамках транзакций. Затем эта статистика самим процессом записывается в разделяемую память, но не чаще, 
чем раз в одну секунду (задано при компиляции). Накопительная статистика запоминается в **PGDATA/pg_stat/** при штатной остановке сервера и считывается при его запуске. 
При аварийной остановке все счетчики сбрасываются.

Обслуживающий процесс может кешировать данные статистики при обращении к ней. Уровнем кеширования управляет параметр stats_fetch_consistency:

- **none** — без кеширования, статистика только в разделяемой памяти;

- **cache** — кешируется статистика по одному объекту;

- **snapshot** — кешируется вся статистика текущей базы данных.

По умолчанию используется значение **cache** — это компромисс между согласованностью и эффективностью.

Закешированная статистика не перечитывается и сбрасывается в конце транзакции или при вызове **pg_stat_clear_snapshot()**.

Из-за задержек и кеширования обслуживающий процесс использует не самую свежую статистику, но обычно это и не требуется.

Практика
--------

**Накопительная статистика**

::

	A=# CREATE DATABASE admin_monitoring;
	CREATE DATABASE

::

	A=# \c admin_monitoring
	You are now connected to database "admin_monitoring" as user "postgres".

1. Включение сбора статистики ввода-вывода:

::

	A=# ALTER SYSTEM SET track_io_timing=on;
	ALTER SYSTEM

	A=# SELECT pg_reload_conf();
	 pg_reload_conf 
	----------------
	 t
	(1 row)

Смотреть на активности сервера имеет смысл, когда какие-то активности на самом деле есть. Чтобы сымитировать нагрузку, 
воспользуемся **pgbench** — штатной утилитой для запуска эталонных тестов.

Сначала утилита создает набор таблиц и заполняет их данными.

::


	admin$ pgbench -i admin_monitoring

	dropping old tables...
	NOTICE:  table "pgbench_accounts" does not exist, skipping
	NOTICE:  table "pgbench_branches" does not exist, skipping
	NOTICE:  table "pgbench_history" does not exist, skipping
	NOTICE:  table "pgbench_tellers" does not exist, skipping
	creating tables...
	generating data (client-side)...
	100000 of 100000 tuples (100%) done (elapsed 0.61 s, remaining 0.00 s)
	vacuuming...
	creating primary keys...
	done in 1.03 s (drop tables 0.00 s, create tables 0.02 s, client-side generate 0.69 s, 
	vacuum 0.14 s, primary keys 0.19 s).

Сброс накопленной ранее статистику по базе данных:
::

	A=# SELECT pg_stat_reset();

	 pg_stat_reset 
	---------------
	 
	(1 row)

А также статистику экземпляра по вводу-выводу:

::

	A=# SELECT pg_stat_reset_shared('io');

	 pg_stat_reset_shared 
	----------------------
	 
	(1 row)

Запуск тестf TPC-B на несколько секунд:

::

	admin$ pgbench -T 10 admin_monitoring

	pgbench (16.9 ))
	starting vacuum...end.
	transaction type: <builtin: TPC-B (sort of)>
	scaling factor: 1
	query mode: simple
	number of clients: 1
	number of threads: 1
	maximum number of tries: 1
	duration: 10 s
	number of transactions actually processed: 1360
	number of failed transactions: 0 (0.000%)
	latency average = 7.352 ms
	initial connection time = 3.828 ms
	tps = 136.022702 (without initial connection time)

Теперь мы можем посмотреть статистику обращений к таблицам в терминах строк:

::

	A=# SELECT *
	FROM pg_stat_all_tables
	WHERE relid = 'pgbench_accounts'::regclass \gx

	-[ RECORD 1 ]-------+------------------------------
	relid               | 16393
	schemaname          | public
	relname             | pgbench_accounts
	seq_scan            | 0
	last_seq_scan       | 
	seq_tup_read        | 0
	idx_scan            | 2720
	last_idx_scan       | 2025-06-23 23:25:35.249459+03
	idx_tup_fetch       | 2720
	n_tup_ins           | 0
	n_tup_upd           | 1360
	n_tup_del           | 0
	n_tup_hot_upd       | 429
	n_tup_newpage_upd   | 931
	n_live_tup          | 0
	n_dead_tup          | 1248
	n_mod_since_analyze | 1360
	n_ins_since_vacuum  | 0
	last_vacuum         | 
	last_autovacuum     | 
	last_analyze        | 
	last_autoanalyze    | 
	vacuum_count        | 0
	autovacuum_count    | 0
	analyze_count       | 0
	autoanalyze_count   | 0

И в терминах страниц:

::

	A=# SELECT *
	FROM pg_statio_all_tables
	WHERE relid = 'pgbench_accounts'::regclass \gx

	-[ RECORD 1 ]---+-----------------
	relid           | 16393
	schemaname      | public
	relname         | pgbench_accounts
	heap_blks_read  | 0
	heap_blks_hit   | 9199
	idx_blks_read   | 274
	idx_blks_hit    | 7032
	toast_blks_read | 
	toast_blks_hit  | 
	tidx_blks_read  | 
	tidx_blks_hit   | 

Существуют аналогичные представления для индексов:

::

	A=# SELECT *
	FROM pg_stat_all_indexes
	WHERE relid = 'pgbench_accounts'::regclass \gx

	-[ RECORD 1 ]-+------------------------------
	relid         | 16393
	indexrelid    | 16407
	schemaname    | public
	relname       | pgbench_accounts
	indexrelname  | pgbench_accounts_pkey
	idx_scan      | 2720
	last_idx_scan | 2025-06-23 23:25:35.249459+03
	idx_tup_read  | 3654
	idx_tup_fetch | 2720

::

	A=# SELECT *
	FROM pg_statio_all_indexes
	WHERE relid = 'pgbench_accounts'::regclass \gx
	-[ RECORD 1 ]-+----------------------
	relid         | 16393
	indexrelid    | 16407
	schemaname    | public
	relname       | pgbench_accounts
	indexrelname  | pgbench_accounts_pkey
	idx_blks_read | 274
	idx_blks_hit  | 7032

Эти представления, в частности, могут помочь определить неиспользуемые индексы. Такие индексы не только бессмысленно занимают место на диске, 
но и тратят ресурсы на обновление при каждом изменении данных в таблице.

Есть также представления для пользовательских и системных объектов (all, user, sys), для статистики текущей транзакции (pg_stat_xact*) и другие.

Можно посмотреть общую статистику по базе данных:

::

	A=# SELECT *
	FROM pg_stat_database
	WHERE datname = 'admin_monitoring' \gx

	-[ RECORD 1 ]------------+------------------------------
	datid                    | 16386
	datname                  | admin_monitoring
	numbackends              | 1
	xact_commit              | 1376
	xact_rollback            | 0
	blks_read                | 276
	blks_hit                 | 26827
	tup_returned             | 20098
	tup_fetched              | 3351
	tup_inserted             | 1360
	tup_updated              | 4081
	tup_deleted              | 0
	conflicts                | 0
	temp_files               | 0
	temp_bytes               | 0
	deadlocks                | 0
	checksum_failures        | 
	checksum_last_failure    | 
	blk_read_time            | 15.291
	blk_write_time           | 1.131
	session_time             | 21463.672
	active_time              | 9224.644
	idle_in_transaction_time | 682.323
	sessions                 | 2
	sessions_abandoned       | 0
	sessions_fatal           | 0
	sessions_killed          | 0
	stats_reset              | 2025-06-23 23:25:25.082128+03

Здесь есть много полезной информации о количестве произошедших взаимоблокировок, зафиксированных и отмененных транзакций, использовании временных файлов, 
ошибках подсчета контрольных сумм. Здесь же хранится статистика общего количества сеансов и количества прерванных по разным причинам сеансов.

Столбец **numbackends** показывает текущее количество обслуживающих процессов, подключенных к базе данных.

Статистика ввода-вывода на уровне сервера доступна в представлении **pg_stat_io**. Например, выполним контрольную точку и посмотрим количество операций чтения и 
записи страниц по типам процессов:

::

	A=# CHECKPOINT;

	CHECKPOINT

::

	A=# SELECT backend_type, sum(hits) hits, sum(reads) reads, sum(writes) writes
	FROM pg_stat_io
	GROUP BY backend_type;

		backend_type     | hits  | reads | writes 
	---------------------+-------+-------+--------
	 background worker   |     0 |     0 |      0
	 client backend      | 27953 |   276 |      0
	 walsender           |     0 |     0 |      0
	 standalone backend  |     0 |     0 |      0
	 autovacuum worker   |   584 |     0 |      0
	 autovacuum launcher |     0 |     0 |      0
	 background writer   |       |       |      0
	 startup             |     0 |     0 |      0
	 checkpointer        |       |       |   2878
	(9 rows)