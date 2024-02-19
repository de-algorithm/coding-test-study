-- 풀이1
with Weather_2 as(
    SELECT *, 
        (SELECT temperature 
        FROM Weather AS B WHERE B.id = A.id-1) AS lag_temp
    FROM Weather AS A 
)

SELECT id FROM Weather_2
WHERE temperature > lag_temp

-- 풀이2
-- SELECT id FROM (SELECT *, lag(temperature) over (order by recordDate) AS lag_temp 
--     FROM Weather) AS Weather2
-- WHERE temperature > lag_temp



-- 풀이3
-- SELECT w1.id
-- FROM Weather w1, Weather w2
-- WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;