WITH title_result AS (
    -- Get the top-rated movie from February 2020
    SELECT Movies.title, C.avg_rate
    FROM Movies
    INNER JOIN (
        SELECT movie_id, AVG(rating) AS avg_rate
        FROM MovieRating
        WHERE DATE_FORMAT(created_at, "%Y-%m") = "2020-02"
        GROUP BY movie_id
    ) C ON Movies.movie_id = C.movie_id
    ORDER BY C.avg_rate DESC, Movies.title
    LIMIT 1
), 
user_result AS (
    -- Get the user with the most movie ratings
    SELECT Users.name
    FROM Users
    INNER JOIN (
        SELECT user_id, COUNT(*) AS CNT
        FROM MovieRating
        GROUP BY user_id
    ) B ON Users.user_id = B.user_id
    ORDER BY B.CNT DESC, Users.name
    LIMIT 1
)
-- Combine the top movie title and top user name into a single column
SELECT name AS results
FROM user_result
UNION ALL
SELECT title AS results
FROM title_result;