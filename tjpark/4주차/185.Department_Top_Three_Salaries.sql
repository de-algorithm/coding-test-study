-- # 각 부서에 연봉 높은 순으로 3명 추출
-- # 부서와 연봉이 같은 사람들은 1명으로 취급
-- # 1823 ms
WITH
A1 AS(
SELECT 
    B.name as Department, 
    A.name as Employee, 
    A.salary as Salary,
    DENSE_RANK() OVER (PARTITION BY B.name ORDER BY A.salary DESC) AS s_rank
FROM Employee A
    INNER JOIN Department B ON A.departmentId = B.id
)
SELECT Department, Employee, Salary
FROM A1
WHERE s_rank <= 3