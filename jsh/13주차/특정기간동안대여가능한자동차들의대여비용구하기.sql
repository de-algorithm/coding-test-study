-- 코드를 입력하세요
SELECT C.CAR_ID, C.CAR_TYPE,ROUND(DAILY_FEE*30 *((100-DISCOUNT_RATE)/100),0) AS 'FEE'
FROM CAR_RENTAL_COMPANY_CAR C
LEFT JOIN (SELECT CAR_TYPE,duration_type,DISCOUNT_RATE 
            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
           WHERE CAR_TYPE IN ('SUV','세단') AND duration_type = '30일 이상'
          ) P ON C.CAR_TYPE = P.CAR_TYPE
WHERE C.CAR_TYPE IN ('세단','SUV') AND C.CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
        WHERE ('2022-11'  BETWEEN DATE_FORMAT(START_DATE,'%Y-%m') AND DATE_FORMAT(END_DATE,'%Y-%m'))
         )
HAVING FEE BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, C.CAR_TYPE, C.CAR_ID DESC