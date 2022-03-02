v.2.0 - без встроенных функций posgresql

## Задача:

1. сгенерировать файл размером ~ 1 GB
2. создать PostgreSQL-таблицу на 1 поле
3. вставить созданный файл в таблицу

## Условия:

1. не использовать ORM
2. не использовать декораторы python
3. файл при загрузке в таблицу не должен сжиматься

### установить виртуальное окружение:
    python3 -m venv env

### запустить виртуальное окружение:
    source env/bin/activate 

### установить зависимости:
    pip install -r requirements.txt

### запустить файл 
    main.py

 ~~P.S.т.к. storage = plain, то TOAST (ни на сжатие ни на отдельное хранение) не применяется.~~

  ## P.S.т.к. STORAGE колонки определн - plain (стр. 37-40), то TOAST (ни на сжатие ни на отдельное хранение) не применяется.