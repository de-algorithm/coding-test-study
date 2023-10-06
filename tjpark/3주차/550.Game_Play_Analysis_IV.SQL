-- # 처음 로그인한 다음 날 다시 로그인한 플레이어의 비율
-- # 소숫점 2자리 기준 반올림
-- # 2일 연속 플레이한 플레이어 수 / 전체 플레이어 수


SELECT ROUND(sum(log_in)/ count(DISTINCT(player_id)),2) as fraction
FROM (
    SELECT 
        player_id,
        DATEDIFF(event_date, MIN(event_date) OVER(PARTITION BY player_id)) = 1 as log_in
    FROM Activity
) A