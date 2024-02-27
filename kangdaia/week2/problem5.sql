/* leetcode
Human_Traffic_of_Stadium
*/
WITH A AS 
(
  SELECT *, id - row_number() over (order by id) as gap
  FROM Stadium
  WHERE people >= 100
)
SELECT id, visit_date, people
FROM A
WHERE gap in 
(
  SELECT gap 
  FROM A 
  GROUP BY gap 
  HAVING COUNT(*) >= 3
)