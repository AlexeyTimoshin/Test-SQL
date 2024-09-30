Для отклика на эту вакансию необходимо ответить на несколько вопросов работодателя.  

У вас есть SQL база данных с таблицами международной частной клиники, которая существует много лет:  
1) Patients(patientId, age)  
2) Visits(visitId, patientId, serviceId, date)  
3) Services(serviceId, cost)  

Напишите четыре SQL запроса дл я расчета следующих метрик. В расчете учитывайте повышенную вероятность коллизий по агрегатам   
различных метрик, например, существует несколько услуг с одинаковой доходностью в промежутке времени.  
А) какую сумму в среднем в месяц тратит:  
- пациент в возрастном диапазоне от 18 до 25 лет включительно  
- пациент в возрастном диапазоне от 26 до 35 лет включительно
```sql
--- 18-25
SELECT AVG(sum_month) as avg_sum_month_18_25
FROM
(SELECT p.patientId,
        EXTRACT(YEAR FROM v.date) AS year,
        EXTRACT(MONTH FROM v.date) AS month,
        SUM(s.cost) sum_month
FROM Patients p
JOIN Visits v ON p.patientId = v.patientId
JOIN Services s ON v.serviceId = s.serviceId
WHERE p.age >= 18 AND p.age <= 25
GROUP BY 1, 2, 3) t

---  26-35

SELECT AVG(sum_month) as avg_sum_month_26_35
FROM
(SELECT p.patientId,
        EXTRACT(YEAR FROM v.date) AS year,
        EXTRACT(MONTH FROM v.date) AS month,
        SUM(s.cost) sum_month
FROM Patients p
JOIN Visits v ON p.patientId = v.patientId
JOIN Services s ON v.serviceId = s.serviceId
WHERE p.age >= 26 AND p.age <= 35
GROUP BY 1, 2, 3) t
```

Б) в каком месяце года доход от пациентов в возрастном диапазоне 35+ самый большой  
```sql
--- решение в лоб - сумма по всем месяцам за все года + проверка что таких месяцев может несколько
WITH cte AS (
SELECT  EXTRACT(MONTH FROM v.date) AS month,
        SUM(s.cost) sum_month
FROM Patients p
JOIN Visits v ON p.patientId = v.patientId
JOIN Services s ON v.serviceId = s.serviceId
WHERE p.age > 35
GROUP BY 1
)

SELECT month
FROM cte
WHERE sum_month IN (
    SELECT MAX(sum_month)
    FROM cte
)

--- получим максимум отдельно по каждому году и месяцу
SELECT year, month,
       MAX(sum_month) OVER(PARTITION BY year) as sum
FROM
(SELECT
        EXTRACT(YEAR FROM v.date) AS year,
        EXTRACT(MONTH FROM v.date) AS month,
        SUM(s.cost) sum_month
FROM Patients p
JOIN Visits v ON p.patientId = v.patientId
JOIN Services s ON v.serviceId = s.serviceId
WHERE p.age > 35
GROUP BY 1, 2) t

```

В) какая услуга обеспечивает наибольший вклад в доход за последний год  
```sql

WITH visitF AS (
SELECT serviceId,
       EXTRACT (YEAR FROM date) year
FROM Visits)

SELECT serviceId
FROM 
(SELECT v.serviceId,
        SUM(s.cost) sum_cst
FROM visitF v
JOIN Services s ON v.serviceId = s.serviceId
WHERE v.year IN (SELECT MAX(year) FROM visitF)
GROUP BY 1) t
ORDER BY sum_cst DESC
LIMIT 1
```

Г) ежегодные топ-5 услуг по доходу и их доля в общем доходе за год  
```sql
WITH visitF AS (
SELECT serviceId,
       EXTRACT (YEAR FROM date) year
FROM Visits)

SELECT  v.serviceId,
        ROUND(SUM(s.cost) OVER(PARTITION BY serviceId)::DECIMAL / SUM(s.cost) OVER(), 2) share 
FROM visitF v
JOIN Services s ON v.serviceId = s.serviceId
WHERE v.year IN (SELECT MAX(year) FROM visitF)
GROUP BY 1
ORDER BY share DESC
LIMIT 5
```
