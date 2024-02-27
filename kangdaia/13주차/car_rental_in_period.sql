SELECT 
    A.CAR_ID, 
    A.CAR_TYPE, 
    ROUND(A.DAILY_FEE * (1 - C.DISCOUNT_RATE / 100) * 30) AS FEE
FROM CAR_RENTAL_COMPANY_CAR A
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.CAR_ID = B.CAR_ID
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C ON A.CAR_TYPE = C.CAR_TYPE
WHERE (
    A.CAR_TYPE = '세단' OR A.CAR_TYPE = 'SUV'
) AND (
    C.DURATION_TYPE = '30일 이상'
)
GROUP BY A.CAR_ID, A.CAR_TYPE, A.DAILY_FEE, C.DISCOUNT_RATE
HAVING 
    MAX(B.END_DATE) <= '2022-11-01' AND 500000 <= FEE AND FEE < 2000000
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC;
/*
chatGPT에게 MYSQL 문법으로 고쳐달라고 요청,
답변:
- 문자열은 작은따옴표(')를 사용하여 A.CAR_TYPE = '세단'과 같이 표현합니다.
- DATE("2022-11-01")는 MySQL에서 '2022-11-01'로 간단히 표현할 수 있습니다.
- GROUP BY 절에는 선택된 모든 컬럼을 포함해야 합니다. MySQL의 엄격한 모드에서는 그룹화되지 않은 컬럼에 대한 셀렉션을 허용하지 않기 때문에 A.CAR_TYPE, A.DAILY_FEE, C.DISCOUNT_RATE를 추가했습니다.
- ORDER BY 절에서 CAR_TYPE 대신 A.CAR_TYPE을 사용하였습니다. 이는 명시적으로 어떤 테이블의 컬럼인지 지정해주는 것이 좋은 관행입니다.
*/