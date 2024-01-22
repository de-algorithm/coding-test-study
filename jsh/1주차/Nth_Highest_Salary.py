# 시작시간 : 2:30
# 끝난시간 : 3:00

# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 

# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+
# Example 2:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+

# Create table If Not Exists Employee (Id int, Salary int)
# Truncate table Employee
# insert into Employee (id, salary) values ('1', '100')
# insert into Employee (id, salary) values ('2', '200')
# insert into Employee (id, salary) values ('3', '300')

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      
    SELECT distinct b.salary
    FROM ( SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk 
            FROM Employee
            ) as b
    WHERE rnk  = N
  );
END

## ROW_NUMBER , RANK, DENSE_RANK의 차이를 알아야 하는 것 같다