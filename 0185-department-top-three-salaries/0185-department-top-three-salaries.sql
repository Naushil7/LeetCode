-- # Write your MySQL query statement below
with cte as
(SELECT *, dense_RANK() OVER (PARTITION BY departmentid ORDER BY salary DESC) AS high
FROM Employee e)

select d.name as Department, c.name as Employee, c.salary as Salary
from cte c
join department d
on c.departmentid = d.id
where c.high <= 3