# Write your MySQL query statement below
with cte as (SELECT lat, lon
FROM Insurance
GROUP BY lat, lon
HAVING COUNT(*) = 1),

cte2 as (select tiv_2015
from insurance
group by tiv_2015
having count(*) > 1
)

-- select *
select round(sum(tiv_2016), 2) as tiv_2016
from insurance i
join cte c
on i.lat = c.lat and i.lon = c.lon
join cte2 c2
on i.tiv_2015 = c2.tiv_2015