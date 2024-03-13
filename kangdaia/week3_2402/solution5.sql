SELECT TB1.id as Id
FROM Weather AS TB1, Weather AS TB2
WHERE DATEDIFF(TB1.recordDate, TB2.recordDate) = 1 AND TB1.temperature - TB2.temperature > 0