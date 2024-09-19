# Write your MySQL query statement below
select p1.product_name, sum(unit) as unit
from products p1
join orders o1
on p1.product_id = o1.product_id
WHERE DATE_FORMAT(order_Date, '%Y-%m') = '2020-02'
group by DATE_format(order_date, '%Y-%m'), p1.product_id
having sum(unit) >= 100