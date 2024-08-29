# Write your MySQL query statement below
select max(num) as num
from
(
    select num
    from mynumbers
    group by num
    having Count(*) = 1
) as A