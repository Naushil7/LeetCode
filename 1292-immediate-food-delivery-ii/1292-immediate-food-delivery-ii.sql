WITH RankedOrders AS (
    SELECT *,
           RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS order_number
    FROM Delivery
)
SELECT ROUND(
    (COUNT(CASE WHEN order_date = customer_pref_delivery_date AND order_number = 1 THEN 1 END) /
    COUNT(CASE WHEN order_number = 1 THEN 1 END)) * 100, 2
) AS immediate_percentage
FROM RankedOrders;
