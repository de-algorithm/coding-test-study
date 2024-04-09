/*
Problem     : https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50
Date        : 2024.04.04
Level       : medium
*/

WITH all_counting AS(
    SELECT user_id, count(*) total_cnt FROM Confirmations
    GROUP BY user_id
),

confirmed_counting AS (
SELECT user_id, count(*) confirmed_cnt FROM Confirmations
WHERE action = 'confirmed'
GROUP BY user_id
)

SELECT s.user_id, 
    ifnull(
        ROUND(ifnull(confirmed_cnt, 0.00)/total_cnt,3),0) confirmation_rate
FROM all_counting ac
LEFT JOIN confirmed_counting cc 
ON ac.user_id = cc.user_id
RIGHT JOIN Signups s
on ac.user_id = s.user_id