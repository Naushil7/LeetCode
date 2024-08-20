# Write your MySQL query statement below
select query_name, 
round(avg(rating/position), 2) as quality, 
round(((select count(rating) from queries q2 where rating < 3 and q2.query_name = q1.query_name)/(select count(rating)))*100, 2)as poor_query_percentage
from queries q1
where query_name is not null
group by query_name