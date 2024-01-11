SELECT A.PRODUCT_ID, A.PRODUCT_NAME, SUM(B.AMOUNT * A.PRICE) AS 'TOTAL_SALES'
FROM FOOD_PRODUCT A
INNER JOIN FOOD_ORDER B
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE DATE_FORMAT(PRODUCE_DATE,'%Y-%m') = "2022-05"
GROUP BY B.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID ASC