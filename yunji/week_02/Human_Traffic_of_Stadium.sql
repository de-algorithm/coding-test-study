/*
Problem     : https://leetcode.com/problems/human-traffic-of-stadium
Date        : 2024.01.29
Runtime     : 669ms (Beats 51.09%)
*/
WITH t1 AS (
SELECT *, id - ROW_NUMBER() OVER() id_diff 
FROM Stadium
WHERE people > 99
)

SELECT id, visit_date, people 
FROM t1 
WHERE id_diff IN (
    SELECT id_diff 
    FROM t1
    GROUP BY id_diff
    HAVING count(*) > 2)
ORDER BY visit_date