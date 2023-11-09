-- # 고객의 처음 주문 건 기준
-- # 주문 날짜와 고객의 배송 원하는 날짜가 같으면 즉시 출고
-- # 즉시 출고를 받는 고객의 비율
-- # 백분율로 나타내며 소수점 2자리까지 표시
-- # 1084ms

SELECT ROUND(SUM(equal_date) / COUNT(DISTINCT customer_id),4) * 100 as immediate_percentage
FROM(
    SELECT 
    *,
    CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END as equal_date,
    ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) as RN
    FROM Delivery
) A
WHERE
    RN = 1