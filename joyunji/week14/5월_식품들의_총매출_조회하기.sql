/*
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/131117
Date        : 2024.01.09
Level       : Level4
*/
SELECT fd.PRODUCT_ID, PRODUCT_NAME, SUM(PRICE*AMOUNT) TOTAL_SALES FROM FOOD_ORDER fd 
INNER JOIN FOOD_PRODUCT fp 
ON fd.PRODUCT_ID = fp.PRODUCT_ID
WHERE LEFT(PRODUCE_DATE, 7) = '2022-05'
GROUP BY fd.PRODUCT_ID
ORDER BY 3 DESC, 1  