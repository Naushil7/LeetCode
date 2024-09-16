# Write your MySQL query statement below
with cte1 as(select requester_id as id, accepter_id
from requestaccepted

union

select accepter_id as id, requester_id
from requestaccepted)

select id, count(*) as num
from cte1
group by id
order by num desc
limit 1
