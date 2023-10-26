WITH A AS (
    SELECT 
    tiv_2016,
    COUNT(CONCAT(lat, lon)) OVER (PARTITION BY CONCAT(lat, lon)) as uniq_cnt,
    COUNT(tiv_2015) OVER (PARTITION BY tiv_2015) as mult_cnt
    FROM Insurance
)
SELECT ROUND(SUM(A.tiv_2016), 2) as tiv_2016
FROM A
WHERE uniq_cnt = 1 and mult_cnt > 1