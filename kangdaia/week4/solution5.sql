/*
row_number는 distinct 전에 계산됨
dense_rank는 distinct 후에 계산됨
*/
SELECT Department, Employee, Salary
FROM (
    SELECT 
    B.name as Department,
    A.name as Employee,
    A.salary as Salary,
    DENSE_RANK() OVER(PARTITION BY B.name ORDER BY A.salary DESC) AS salary_rank
    FROM Employee A
    INNER JOIN
    Department B
    ON A.departmentId = B.id
) TEMP
WHERE salary_rank <= 3