# Write your MySQL query statement below
with cte as
(select *, count(email) as duplicate
from person
group by email)

select email
from cte 
where duplicate > 1