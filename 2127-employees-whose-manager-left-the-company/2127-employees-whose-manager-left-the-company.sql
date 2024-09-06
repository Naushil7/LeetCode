# Write your MySQL query statement below
select employee_id
from employees
where salary < 30000 
and manager_id is not Null 
AND manager_id NOT IN (SELECT employee_id FROM employees)
order by employee_id