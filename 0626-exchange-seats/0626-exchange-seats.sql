# Write your MySQL query statement below
with cte as 
(select *,
LEAD(id) over(order by id) as next, 
Lag(id) over(order by id) as prev
from seat)


select case 
when ((id%2 = 1) and next is Not null) then next
when (id%2 = 0) then prev
else id
end as id, student
from cte
order by id
