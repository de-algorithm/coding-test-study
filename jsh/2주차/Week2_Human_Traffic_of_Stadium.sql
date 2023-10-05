# HARD
# start > 17:30
# end > 18:20


## 접근하기
## id와 date기준으로 오름차순이 되어있기 때문에 
## 100명이상으로 필터링을 한 후, row_number를 쓰면 순서대로 숫자가 다시 나타나게 될 것이다.
## 이 숫자와 id를 서로 비교해가면 연속된 구간을 찾을 수 있을 거라 생각.

# 1. 연속되는 구간찾기
# SELECT id,ROW_NUMBER() OVER (ORDER BY id) AS grp_num, visit_date, people,id - ROW_NUMBER() OVER (ORDER BY id) AS grp_num
# FROM Stadium
# WHERE people >= 100


# 2. 연속되는 구간 중 3번이상 연속되는 곳의 grp_num 찾기
# SELECT grp_num
#     FROM (
#         SELECT id - ROW_NUMBER() OVER (ORDER BY id) AS grp_num
#         FROM Stadium
#         WHERE people >= 100
#     ) AS a
#     GROUP BY grp_num
#     HAVING COUNT(*) >= 3


# 3. 3번이상 연속되는 곳의 grp_num을 가지고 있는 값만 select
SELECT a.id, a.visit_date, a.people
FROM (
    SELECT id, visit_date, people, id - ROW_NUMBER() OVER (ORDER BY id) AS grp_num
    FROM Stadium
    WHERE people >= 100
) AS a
WHERE a.grp_num IN (
    SELECT grp_num
    FROM (
        SELECT id - ROW_NUMBER() OVER (ORDER BY id) AS grp_num
        FROM Stadium
        WHERE people >= 100
    ) AS b
    GROUP BY grp_num
    HAVING COUNT(*) >= 3
)
ORDER BY a.visit_date;
