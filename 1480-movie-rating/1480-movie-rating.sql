WITH cte1 AS (
    SELECT m1.user_id, u.name, COUNT(m1.movie_id) AS movie_count
    FROM MovieRating m1
    JOIN users u ON m1.user_id = u.user_id
    GROUP BY m1.user_id, u.name
),
cte2 AS (
    SELECT m2.title, AVG(m1.rating) AS avg_rating
    FROM MovieRating m1
    JOIN movies m2 ON m1.movie_id = m2.movie_id
    WHERE m1.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m2.title
)

(SELECT name AS results
FROM cte1
WHERE movie_count = (SELECT MAX(movie_count) FROM cte1)
ORDER BY name
LIMIT 1)

UNION ALL

(SELECT title AS results
FROM cte2
WHERE avg_rating = (SELECT MAX(avg_rating) FROM cte2)
ORDER BY title
LIMIT 1)