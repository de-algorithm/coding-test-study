
# Write your MySQL query statement below

SELECT request_at AS Day,
  ROUND(
         SUM(CASE WHEN status = 'cancelled_by_driver' OR status = 'cancelled_by_client' THEN 1 ELSE 0 END) / COUNT(*), 2
       ) AS 
       "Cancellation Rate"
From Trips
where 
  request_at between  
  "2013-10-01" 
  and 
  "2013-10-03"
  and
  client_id in (
  select users_id
  from Users
  where banned = 'No'
  ) 
  and 
  driver_id in (
  select users_id
  from Users
  where banned = 'No'
  )
Group by request_at


# 실패했었던 test case # 11
# 이유 : 날짜 between 안씀
# Input
# Trips =
# | id | client_id | driver_id | city_id | status              | request_at |
# | -- | --------- | --------- | ------- | ------------------- | ---------- |
# | 1  | 1         | 10        | 1       | cancelled_by_client | 2013-10-04 |
# Users =
# | users_id | banned | role   |
# | -------- | ------ | ------ |
# | 1        | No     | client |
# | 10       | No     | driver |

# Use Testcase
# Output
# | Day        | Cancellation Rate |
# | ---------- | ----------------- |
# | 2013-10-04 | 1                 |
# Expected
# | Day | Cancellation Rate |
# | --- | ----------------- |

# 실패했었던 test case # 12
# 이유 : Client_id만 where에 씀 
# 허허