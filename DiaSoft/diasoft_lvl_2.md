### 1. Написать запрос, который из таблицы A возвращает все строки, для которых значение столбца name отсутсвует в таблице B.

A
|id| name|
|---|---|
|1| AAA|
|2| BBB|
|3| CCC|
|4| DDD|
|5| EEE|

B
|id| name|
|---|---|
|1| null|
|2| BBB|
|3| CCC|
|4| CCC|
|5| null|
|6| DDD|

Result
|id| name|
|---|---|
|1| AAA|
|5| EEE|

<details>
  <summary> Код для бд </summary>
  
  ``` SQL
CREATE TABLE A (id INT, name VARCHAR(5));
INSERT INTO a (id, name) VALUES
(1, 'AAA'),
(2, 'BBB'),
(3, 'CCC'), 
(4, 'DDD'),
(5, 'EEE');

CREATE TABLE B (id INT, name VARCHAR(5));
INSERT INTO b (id, name) VALUES
(1, null),
(2, 'BBB'),
(3, 'CCC'),
(4, 'CCC'),
(5, null),
(6, 'DDD');
  ```
</details>

Решение
```sql
SELECT a.id, a.name
FROM a
JOIN b as b_filt ON a.id = b_filt.id AND b_filt.name is null
```

### 2. Таблица A содержит следующие данные:

A
|id| name|
|---|---|
|1| AAA|
|2| BBB|
|3| CCC|

Какой результат вернет каждый из шести следующих запросов? Опишите, почему сервер вернет такой результат.  
Примеры данного кода в Postgresql не работают. 
```sql
-- вариант A
declare @name; select @name = 'XXXX'
select @name = name from A where id = 0
print @name
go
-- Вернёт ошибку из за ошибки синтаксиса

-- вариант B
declare @name; select @name = 'XXXX'
select @name = name from A where id = 1
print @name
go
-- Вернёт ошибку из за ошибки синтаксиса

-- вариант C
declare @name; select @name = 'XXXX'
select @name = name from A where id = 2
print @name
go
-- Вернёт ошибку из за ошибки синтаксиса

-- вариант D
declare @name; select @name = 'XXXX'
set @name = (select name from A where id = 0)
print @name
go
-- вариант E
declare @name; select @name = 'XXXX'
set @name = (select name from A where id = 1)
print @name
go
-- вариант F
declare @name; select @name = 'XXXX'
set @name = (select name from A where id = 2)
print @name
go
```

### 3. Опишите отличия и особенности следующих команд delete from A и truncate table A?

Delete FROM удалит записи из таблицы, Truncate удалит полностью таблицу и создаст её заново пустую.  

### 4. (T-SQL) В таблице A (столбец id – integer identity primary key) было три строки. Мы выполнили следующий скрипт

```sql
insert A(name) values('DDD')
print @@identity
insert A(name) values('EEE')
print @@identity
go
```
Результат, выводимый скриптом:  
4
2

Объясните, чем может быть вызван этот неожиданный результат? Как добиться правильного результата (=5) во втором случае?  
Состояние таблицы:  
A до вставки  
|id| name|
|---|---|
|1| AAA|
|2| BBB|
|3| CCC|

А после вставки  
|id| name|
|---|---|
|1| AAA|
|2| BBB|
|3| CCC|
|4| DDD|
|5| EEE|


### 5. (T-SQL) Найдите ошибку в следующем скрипте: 
```sql
begin transaction A
insert A(id,name) values(1,'AAAA')
  begin transaction
  save transaction B
  insert B(id,name) values(1,'AAAA')
  if @@error <> 0 rollback transaction B else commit transaction B
commit transaction A
```
