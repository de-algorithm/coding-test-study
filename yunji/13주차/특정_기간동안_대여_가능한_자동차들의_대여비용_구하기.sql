/*
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/157339
Date        : 2023.12.21
Level       : Level4
*/

/*
2023-12-21 풀이
- 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중
    2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 
    30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차
- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력
- 대여금액 DESC, 자동차 종류 ASC, 자동차 ID DESC 
*/
    
WITH BASE AS (
        SELECT *
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
        WHERE CAR_ID NOT IN (
            SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE '2022-11' BETWEEN DATE_FORMAT(START_DATE, '%Y-%m') 
                AND DATE_FORMAT(END_DATE, '%Y-%m')
            ) 
        ),
        
    BASE2 AS (
        SELECT BASE.CAR_ID, CC.CAR_TYPE, DAILY_FEE, DISCOUNT_RATE FROM BASE 
        LEFT JOIN CAR_RENTAL_COMPANY_CAR CC 
        ON BASE.CAR_ID = CC.CAR_ID
        LEFT JOIN (
            SELECT CAR_TYPE, DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
            WHERE DURATION_TYPE = '30일 이상') CDP
        ON CC.CAR_TYPE = CDP.CAR_TYPE
        WHERE CC.CAR_TYPE = '세단' OR CC.CAR_TYPE ='SUV'
        )

SELECT DISTINCT CAR_ID, CAR_TYPE, ROUND((DAILY_FEE*30)*(1-DISCOUNT_RATE*0.01),0) AS FEE 
FROM BASE2
WHERE ROUND((DAILY_FEE*30)*(1-DISCOUNT_RATE*0.01),0) >= 500000 
    AND ROUND((DAILY_FEE*30)*(1-DISCOUNT_RATE*0.01),0) < 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC