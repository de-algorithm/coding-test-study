SELECT ROUND(T.player_cnt / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM 
(
  SELECT COUNT(DISTINCT A.player_id) AS player_cnt
  FROM Activity A, 
  (
    SELECT player_id, MIN(event_date) AS start_date
    FROM Activity
    GROUP BY player_id
  ) B
  WHERE DATEDIFF(event_date, start_date) = 1 AND A.player_id = B.player_id
) T