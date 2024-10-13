Для отклика на эту вакансию необходимо ответить на несколько вопросов работодателя.  

У вас есть SQL база данных с таблицами международной частной клиники, которая существует много лет:  
1) Patients(patientId, age)  
2) Visits(visitId, patientId, serviceId, date)  
3) Services(serviceId, cost)


<details>
<summary>Код для бд </summary>

```sql
CREATE TAble patients (
    patientId INT,
    age int
);
CREATE TAble visits (
    visitId INT, 
    patientId INT,
    serviceId INT,
    date date
);

CREATE TAble services (
   serviceId INT,
   cost INT
);

INSERT INTO patients(patientId, age) VALUES
(1, 48),
(2, 35),
(3, 51),
(4, 40),
(5, 27),
(6, 42),
(7, 18),
(8, 41),
(9, 48),
(10, 35),
(11, 47),
(12, 32),
(13, 53),
(14, 18),
(15, 27),
(16, 46),
(17, 41),
(18, 28),
(19, 39),
(20, 31),
(21, 21),
(22, 54),
(23, 30),
(24, 22),
(25, 50),
(26, 39),
(27, 43),
(28, 23),
(29, 19),
(30, 21);


INSERT INTO Services(serviceId, cost) VALUES
(1, 683),
(2, 1519),
(3, 1410),
(4, 1054),
(5, 756),
(6, 1629),
(7, 1335),
(8, 205),
(9, 1594),
(10, 1120),
(11, 1565),
(12, 756),
(13, 1301),
(14, 937),
(15, 742),
(16, 465),
(17, 852),
(18, 281),
(19, 1745),
(20, 305);

INSERT INTO visits(visitId, patientId, serviceId, date) VALUES
(1, 11, 20, '2022-8-11'),
(2, 7, 20, '2021-2-8'),
(3, 11, 13, '2021-10-19'),
(4, 5, 18, '2022-12-9'),
(5, 9, 11, '2022-2-4'),
(6, 24, 19, '2022-3-12'),
(7, 18, 5, '2021-7-11'),
(8, 10, 12, '2021-6-17'),
(9, 20, 15, '2019-3-20'),
(10, 13, 7, '2021-10-12'),
(11, 20, 12, '2020-5-11'),
(12, 11, 13, '2019-9-11'),
(13, 21, 18, '2019-11-17'),
(14, 4, 9, '2020-8-3'),
(15, 22, 10, '2020-8-8'),
(16, 10, 3, '2020-4-7'),
(17, 9, 4, '2020-10-6'),
(18, 16, 10, '2022-3-30'),
(19, 16, 13, '2022-8-13'),
(20, 12, 9, '2020-4-19'),
(21, 17, 16, '2021-6-13'),
(22, 10, 5, '2019-2-25'),
(23, 22, 10, '2022-11-10'),
(24, 29, 16, '2020-12-27'),
(25, 17, 14, '2021-3-9'),
(26, 14, 14, '2019-3-2'),
(27, 15, 4, '2021-4-6'),
(28, 7, 4, '2022-9-16'),
(29, 10, 20, '2019-4-5'),
(30, 27, 8, '2022-9-30'),
(31, 9, 17, '2021-4-5'),
(32, 30, 7, '2019-4-9'),
(33, 2, 18, '2022-2-16'),
(34, 20, 17, '2020-10-27'),
(35, 28, 2, '2022-5-1'),
(36, 16, 13, '2021-7-3'),
(37, 3, 18, '2022-9-26'),
(38, 27, 18, '2022-9-1'),
(39, 28, 17, '2021-7-29'),
(40, 5, 1, '2021-2-17'),
(41, 22, 20, '2021-5-8'),
(42, 10, 14, '2021-9-24'),
(43, 13, 17, '2019-11-22'),
(44, 2, 10, '2021-12-10'),
(45, 12, 3, '2019-1-4'),
(46, 26, 5, '2019-10-5'),
(47, 5, 17, '2020-3-18'),
(48, 27, 12, '2020-7-1'),
(49, 22, 5, '2021-8-19'),
(50, 15, 11, '2020-5-25'),
(51, 1, 10, '2022-7-7'),
(52, 6, 1, '2021-6-10'),
(53, 4, 20, '2022-6-14'),
(54, 12, 11, '2019-10-10'),
(55, 18, 17, '2019-5-20'),
(56, 28, 18, '2021-3-30'),
(57, 27, 2, '2021-4-30'),
(58, 18, 7, '2019-2-3'),
(59, 20, 6, '2022-11-11'),
(60, 9, 2, '2022-4-30'),
(61, 12, 11, '2021-1-21'),
(62, 29, 11, '2022-4-28'),
(63, 8, 20, '2019-2-22'),
(64, 16, 16, '2020-9-7'),
(65, 22, 15, '2022-12-11'),
(66, 7, 5, '2020-9-16'),
(67, 23, 15, '2020-2-7'),
(68, 21, 14, '2020-3-9'),
(69, 20, 3, '2021-8-30'),
(70, 22, 15, '2019-7-21'),
(71, 13, 7, '2020-10-21'),
(72, 6, 19, '2020-2-18'),
(73, 23, 6, '2021-11-19'),
(74, 22, 6, '2019-4-16'),
(75, 24, 16, '2020-3-30'),
(76, 3, 15, '2020-3-30'),
(77, 16, 5, '2021-9-18'),
(78, 20, 8, '2021-5-3'),
(79, 13, 6, '2021-9-29'),
(80, 19, 1, '2022-10-2'),
(81, 15, 17, '2020-4-21'),
(82, 14, 18, '2020-11-2'),
(83, 22, 1, '2019-2-24'),
(84, 18, 5, '2022-5-18'),
(85, 7, 3, '2022-11-30'),
(86, 23, 18, '2019-9-6'),
(87, 26, 10, '2019-3-30'),
(88, 13, 1, '2021-1-5'),
(89, 4, 3, '2019-5-25'),
(90, 29, 12, '2021-5-24');
```
</details>

Напишите четыре SQL запроса дл я расчета следующих метрик. В расчете учитывайте повышенную вероятность коллизий по агрегатам   
различных метрик, например, существует несколько услуг с одинаковой доходностью в промежутке времени.  
А) какую сумму в среднем в месяц тратит:  
- пациент в возрастном диапазоне от 18 до 25 лет включительно  
- пациент в возрастном диапазоне от 26 до 35 лет включительно
```sql
--- 18-25
SELECT ROUND(AVG(sum_month), 3) as avg_sum_month_18_25
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

SELECT ROUND(AVG(sum_month),  3) as avg_sum_month_26_35
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
    FROM cte)

--- получим максимум отдельно по каждому году и месяцу

WITH cte AS
(SELECT year, month,
       sum_month,
       MAX(sum_month) OVER(PARTITION BY YEAR)
FROM
(   SELECT
        EXTRACT(YEAR FROM v.date) AS year,
        EXTRACT(MONTH FROM v.date) AS month,
        SUM(s.cost) sum_month
	FROM Patients p
	JOIN Visits v ON p.patientId = v.patientId
	JOIN Services s ON v.serviceId = s.serviceId
	WHERE p.age > 35
GROUP BY 1, 2) t) 

SELECT 
	   CONCAT(year,'-', month) year_month,
       sum_month
FROM cte
WHERE sum_month = max


```

В) какая услуга обеспечивает наибольший вклад в доход за последний год  

```sql
WITH visitF AS (
SELECT serviceId,
       EXTRACT (YEAR FROM date) as year
FROM Visits)

SELECT serviceId, sum_cst
FROM 
(	SELECT v.serviceId,
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
       EXTRACT (YEAR FROM date) as year
FROM Visits)

SELECT  v.serviceId,
        ROUND(SUM(s.cost) OVER(PARTITION BY v.serviceId)::DECIMAL / SUM(s.cost) OVER(), 3) as share 
FROM visitF v
JOIN Services s ON v.serviceId = s.serviceId
WHERE v.year IN (SELECT MAX(year) FROM visitF)
GROUP BY 1, s.cost
ORDER BY share DESC
LIMIT 5
```
