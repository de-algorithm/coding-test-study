# id 3개 연속, 100명이 넘는 경우를 출력
WITH
# 100개 이상 데이터 추출
A1 AS(
    SELECT * 
    FROM Stadium
    WHERE people >= 100
),
# 연속된 id 추출
A2 AS(
    SELECT
        A.id as id1,
        B.id as id2,
        C.id as id3
    FROM A1 A
        INNER JOIN A1 B ON A.id = B.id + 1
        INNER JOIN A1 C ON A.id = C.id + 2
),
# 연속된 id에 해당되는 id 합치고 중복 제거
A3 AS(
    SELECT id1 as id FROM A2
    UNION
    SELECT id2 as id FROM A2
    UNION
    SELECT id3 as id FROM A2
)
# 연속된 id 추출
SELECT
    A.*
FROM A1 A
    INNER JOIN A3 B ON A.id = B.id



