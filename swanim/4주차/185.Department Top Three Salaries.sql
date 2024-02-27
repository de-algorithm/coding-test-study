select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e
left join Department d on e.departmentId = d.id
where e.salary in (
  select * from(
  select distinct(Salary)
  from Employee
  where d.id = departmentId
  order by Salary desc limit 3
  ) as subquery
) ;