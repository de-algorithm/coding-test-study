/*
Problem     : https://leetcode.com/problems/nth-highest-salary
Date        : 2023.09.19
Runtime     : 683ms (Beats 89.43%)
*/
SELECT salary FROM (
    SELECT id, salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS num
    FROM Employee
    ORDER BY num) A
    WHERE num = N 
    LIMIT 1;