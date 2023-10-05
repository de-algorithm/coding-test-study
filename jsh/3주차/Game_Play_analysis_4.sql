# Medium# start > 23.10.05 16:30
# end

# sql중 날짜 차이를 나타내는 datediff라는 것이 있었던 것으로 기억한다. 근데 안썼따

# 1. row_num을 통해 연속된 날짜들 나타내는 쿼리
# SELECT player_id, event_date, event_date - ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS grp_num
# FROM Activity




# 2. 2일 연속된 날짜가 있는 id만 개수 나타내기
# SELECT COUNT(DISTINCT(player_id))
# FROM (
#     SELECT player_id, event_date, event_date - ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS grp_num
#     FROM Activity
# ) a
# GROUP BY player_id, grp_num
# HAVING COUNT(grp_num) >= 2 



# 3. 전체 id 중 2일연속된 날짜가 있는 id 개수만큼 나누기 진행시키기
SELECT TRUNCATE((     
    SELECT COUNT(DISTINCT(0))
        FROM (
            SELECT player_id, event_date - ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS grp_num
            FROM Activity
        ) a
        GROUP BY player_id, grp_num
        HAVING COUNT(grp_num) > 1
    ) / count(distinct(player_id)), 2) as fraction
FROM activity 