/*
Problem     : https://leetcode.com/problems/rank-scores/description/
Date        : 2023.10.16
Runtime     : 4935s (Beats 84.45%)
*/

SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
FROM Scores
ORDER BY 'rank' 