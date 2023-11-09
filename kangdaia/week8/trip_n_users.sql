WITH temp AS 
(
    SELECT * 
    FROM Trips
    WHERE Client_Id NOT IN 
    (
        SELECT Users_Id 
        FROM Users 
        WHERE Banned = 'Yes'
    )
    AND Driver_Id NOT IN 
    (
        SELECT Users_Id 
        FROM Users 
        WHERE Banned = 'Yes'
    )
)
SELECT Request_at AS Day,
round(avg(case when Status = 'completed' then 0 else 1 end),2) as 'Cancellation Rate'
FROM temp
GROUP BY Day
HAVING Day between '2013-10-01' and '2013-10-03'