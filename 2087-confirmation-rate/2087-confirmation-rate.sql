SELECT 
    s.user_id,
    Round(IFNULL(
        (COUNT(CASE WHEN c.action = 'confirmed' THEN 1 END) * 1.0 / 
        (COUNT(c.action))),
        0
    ),2) AS confirmation_rate
FROM signups s
LEFT JOIN confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id
ORDER BY confirmation_rate ASC;
