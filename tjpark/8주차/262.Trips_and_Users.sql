-- # 모수 = client, driver 모두 ban되지 않은 유저
-- # 2013-10-01 ~ 03 날짜 별 취소한 모수 / 모수의 전체
-- # 소숫점 2자리까지 출력
-- # 실행시간 961ms

WITH
NO_BANNED_T AS(
    SELECT *
    FROM Users
    WHERE banned = 'No'
),
Final AS(
    SELECT 
        request_at,
        COUNT(1) as total,
        SUM(CASE WHEN status LIKE 'cancelled%' THEN 1 ELSE 0 END) as cancle
    FROM Trips A
        INNER JOIN NO_BANNED_T B ON A.client_id = B.users_id 
        INNER JOIN NO_BANNED_T C ON A.driver_id = C.users_id
    WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY
        request_at
)

SELECT request_at as Day, ROUND(cancle / total, 2) as 'Cancellation Rate'
FROM Final