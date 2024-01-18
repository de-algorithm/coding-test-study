/*ORDER BY 문과 한줄로 코드를 만들었더니 최소 time complexity가 나옴??*/
SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) AS "rank" FROM Scores