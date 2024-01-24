/*
Problem     : https://leetcode.com/problems/department-top-three-salaries/
Date        : 2023.10.08
Runtime     : 1593ms (Beats 89.15%)
*/

SELECT Department, Employee, salary Salary FROM (
    SELECT e.name Employee, salary, d.id, d.name Department, 
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS seq
    FROM Employee e
    LEFT JOIN Department d
    ON e.departmentId = d.id) r
WHERE seq BETWEEN 1 AND 3