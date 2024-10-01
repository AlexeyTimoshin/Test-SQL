### 1. Написать запрос, котрый из таблиц A и B (столбец id – integer identity primary key) вернет все строки таблицы A, отсутствующие в таблице B и все строки таблицы B, отсутствующие в таблице A. Сформировать столбец remark, как показано в примере

A  
|id|name|
|---|---|
|1|AAA|
|2|BBB|
|3|CCC|
|4|DDD|
|5|EEE|
|6|FFF|

B  
|id|name|
|---|---|
|4|DDD|
|5|EEE|
|6|FFF|
|7|GGG|
|8|HHH|
|9|III|

Результат  

|id|name|remark|
|---|---|---|
|1|AAA|Нет в В|
|2|BBB|Нет в В|
|3|CCC|Нет в В|
|7|GGG|Нет в А|
|8|HHH|Нет в А|
|9|III|Нет в А|

Код для бд  
```sql 
CREATE TABLE  a (id int PRIMARY Key, name Varchar(5));
CREATE TABLE  b (id int PRIMARY Key, name Varchar(5));
INSERT INTO A (id, Name) VALUES 
(1,	'AAA'),
(2,	'BBB'),
(3,	'CCC'),
(4,	'DDD'),
(5,	'EEE'),
(6,	'FFF');
INSERT INTO b (id, Name) VALUES 
(4,	'DDD'),
(5,	'EEE'),
(6,	'FFF'),
(7,	'GGG'),
(8,	'HHH'),
(9,	'III');
```

#### Решение 
 
```sql
--- решение через множества
WITH cte as (
	 SELECT * FROM a 
  INTERSECT 
  SELECT * FROM B
)

SELECT *, 'Нет в В' as remark FROM a
WHERE (id, name) NOT IN (SELECT * FROM cte)
UNION 
SELECT *, 'Нет в A' as remark FROM b
WHERE (id, name) NOT IN (SELECT * FROM cte)
ORDER BY 1
```

### 2. Написать запрос, который из таблицы A вернет неуникальные значения столбца name.

A  
|name|
|---|
|AAA|
|BBB|
|AAA|
|CCC|
|BBB|
|DDD|

Результат  
|name|
|---|
|AAA|
|BBB|

Код для бд  
```sql 
CREATE TABLE  A (name Varchar(5));
INSERT INTO A (Name) VALUES 
('AAA'),
('BBB'),
('AAA'),
('CCC'),
('BBB'),
('DDD');
```

#### Решение 
 
```sql 

```

### 3 Написать запрос, который из таблицы A (столбец id – integer identity primary key) удалит все более поздние неуникальные по столбцу name строки.

A  
|id|name|
|---|---|
|1|AAA|
|2|BBB|
|3|AAA|
|4|CCC|
|5|BBB|
|6|DDD|

Результат  
|id|name|
|---|---|
|1|AAA|
|2|BBB|
|4|CCC|
|6|DDD|

Код для бд  
```sql 
CREATE TABLE  A (id INT PRIMARY KEY, name Varchar(5));
INSERT INTO A (id, Name) VALUES 
(1, 'AAA'),
(2, 'BBB'),
(3, 'AAA'),
(4, 'CCC'),
(5, 'BBB'),
(6, 'DDD');
```

#### Решение 
 
```sql 

```

### 4 Написать запрос, который на основе данных таблицы A вернет следующие значения:
  • минимальное и максимальной значение, сумму по столбцу amount;  
  • сумму всех отрицательных и сумму всех положительных значений amount;  
  • число уникальных значений в столбце amount.  
 
A  
|id|amount|
|---|---|
|1|100|
|2|200|
|3|300|
|4|-100|
|5|200|
|6|300|
|7|-100|

Результат  
min|max|sum|sum_-|sum_+|uniqe|
---|---|---|---|---|---|
-100|300|900|-200|1100|4|

Код для бд  
```sql 
CREATE TABLE a (id INT PRIMARY KEY, amount);
INSERT INTO a(id, amount) VALUES 
(1, 100),
(2, 200),
(3, 300),
(4, -100),
(5, 200),
(6, 300),
(7, -100);
```

#### Решение 
 
```sql 

```

### 5 Написать запрос, который из двух таблиц A и B вернет все строки, в столбце name которых есть подстрока 'иван'.

A  
|name|
|---|
|ОАО "Мосэнерго"|
|ЗАО "Ивановохлеб"|
|ЗАО "Туламебель"|

B  
|name|
|---|
|Смирнов Иван|
|Иванов Петр|
|Сидорова Анна|

Результат  
|name|
|---|
|ЗАО "Ивановохлеб"|
|Смирнов Иван|
|Иванов Петр|

Код для бд  
```sql 
CREATE TABLE  A (name Varchar(100));
CREATE TABLE  b (name Varchar(100));
INSERT INTO  A (name) VALUES 
('ОАО "Мосэнерго"'),
('ЗАО "Ивановохлеб"'),
('ЗАО "Туламебель"');
INSERT INTO  b (name) VALUES
('ЗАО "Ивановохлеб"'),
('Смирнов Иван'),
('Иванов Петр');
```

#### Решение 
 
```sql 

```
