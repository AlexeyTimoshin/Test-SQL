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

Решение
```sql
```

### 2. Таблица A содержит следующие данные:

A
|id| name|
|---|---|
|1| AAA|
|2| BBB|
|3| CCC|

Какой результат вернет каждый из шести следующих запросов? Опишите, почему сервер вернет такой результат.
```sql
-- вариант A
declare @name; select @name = 'XXXX'
select @name = name from A where id = 0
print @name
go
-- вариант B
declare @name; select @name = 'XXXX'
select @name = name from A where id = 1
print @name
go
-- вариант C
declare @name; select @name = 'XXXX'
select @name = name from A where id = 2
print @name
go
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
