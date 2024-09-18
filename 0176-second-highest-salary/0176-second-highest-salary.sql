# Write your MySQL query statement below
WITH cte1 AS (
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 2
)

SELECT 
    CASE 
        WHEN COUNT(*) < 2 THEN NULL
        ELSE MIN(salary)
    END AS SecondHighestSalary
FROM cte1;
