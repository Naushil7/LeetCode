# Write your MySQL query statement below
select *
from users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$';