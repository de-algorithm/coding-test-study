-- 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서
-- 대여 기록 별로 대여 금액(FEE)을 구하여
-- 대여 기록 ID와 대여 금액 리스트를 출력
-- 대여 금액을 기준으로 내림차순 정렬
-- 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬

WITH cte AS (
    SELECT car_type, daily_fee, history_id, end_date, start_date,
        CASE
            WHEN DATEDIFF(END_DATE, START_DATE) > 6 AND DATEDIFF(END_DATE, START_DATE) < 30 THEN '7일 이상'
            WHEN DATEDIFF(END_DATE, START_DATE) > 29 AND DATEDIFF(END_DATE, START_DATE) < 90 THEN '30일 이상'
            WHEN DATEDIFF(END_DATE, START_DATE) > 89  THEN '90일 이상'
            ELSE NULL
        END PEROID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY rh
    LEFT JOIN CAR_RENTAL_COMPANY_CAR cc 
    ON rh.CAR_ID = cc.CAR_ID
    WHERE CAR_TYPE = '트럭'
)

SELECT history_id,
ROUND(daily_fee*(1-(IFNULL(discount_rate*0.01,0)))*(DATEDIFF(END_DATE, START_DATE)+1),0) FEE
FROM cte
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN cdp
ON cte.car_type = cdp.car_type AND cte.peroid = cdp.duration_type
ORDER BY 2 DESC, 1 DESC

