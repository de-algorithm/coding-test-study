-- # 0시-23시 (데이터에 없는 시간도 출력)
-- # 각 시간대별로 입양이 몇 건이나 발생했는지 조회
-- # 시간대 순으로 정렬

-- UNION 사용
SELECT H.HOUR, IFNULL(AO.COUNT, 0) COUNT
FROM(
    SELECT 0 HOUR 
    UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4
    UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8
    UNION SELECT 9 UNION SELECT 10 UNION SELECT 11 UNION SELECT 12
    UNION SELECT 13 UNION SELECT 14 UNION SELECT 15 UNION SELECT 16
    UNION SELECT 17 UNION SELECT 18 UNION SELECT 19 UNION SELECT 20
    UNION SELECT 21 UNION SELECT 22 UNION SELECT 23) H
    LEFT JOIN(
        SELECT HOUR(DATETIME) HOUR, COUNT(1) COUNT 
        FROM ANIMAL_OUTS
        GROUP BY HOUR
    )AO
    ON H.HOUR = AO.HOUR




-- SET 변수 사용
SET @HOUR = -1;
SELECT @HOUR := @HOUR + 1 HOUR,
    (SELECT COUNT(*) FROM ANIMAL_OUTS
        WHERE HOUR(DATETIME) = @HOUR) COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23
