# Write your MySQL query statement below
with cte as 
(select *, 
SUM(weight) OVER (ORDER BY turn) AS cumulative_weight, 
RANK() OVER (ORDER BY turn) AS Ranking
from queue) 

select person_name
from cte
where cumulative_weight <= 1000
order by ranking desc
limit 1