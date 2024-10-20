# Write your MySQL query statement below
with cte as (
select d.name as Department, e.name as Employee, Salary, rank() over(partition by d.id order by salary desc) as Top_salary 
from employee e
join department d
on e.departmentid = d.id)

select Department, Employee, Salary
from cte 
where Top_salary = 1