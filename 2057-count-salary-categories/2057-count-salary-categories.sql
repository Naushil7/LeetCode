# Write your MySQL query statement below
-- -- Without Includsion
-- select 
-- CASE
--     when income < 20000 then "Low Salary"
--     when income between 20000 and 50000 then "Average Salary"
--     when income > 50000 then "High Salary"
-- END as category,
-- Count(*) as accounts_count 
-- from Accounts
-- group by category

select "High Salary" as category,
sum(case when income > 50000 then 1 Else 0 END) as accounts_count
from Accounts
union
select "Average Salary" as category,
sum(case when income between 20000 and 50000 then 1 Else 0 END) as accounts_count
from Accounts
union
select "Low Salary" as category,
sum(case when income < 20000 then 1 Else 0 END) as accounts_count
from Accounts