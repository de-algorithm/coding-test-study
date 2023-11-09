-- # 1. tiv_2015가 같은 값 2개 이상
-- # 2. 위도, 경도가 고유한 사람
-- # 3. 2016 합계 (소수점 둘째자리 반올림)
-- # 수행시간 829ms
WITH
-- # 중복된 값이 있는 tiv_2015
T1 AS(
  SELECT tiv_2015, COUNT(tiv_2015)
  FROM Insurance
  GROUP BY tiv_2015
  HAVING COUNT(tiv_2015) >=2 
),
-- # 위도, 경도 고유값을 추출 하기 위한 테이블 생성
T2 AS(
  SELECT *, CONCAT(CAST(lat as CHAR),CAST(lon as CHAR)) as gio
  FROM Insurance 
),
-- 위도, 경도 고유한 값 추출
T3 AS(
  SELECT *
  FROM T2 A
    INNER JOIN (SELECT gio as dist_gio
                FROM T2
                GROUP BY gio
                HAVING COUNT(gio) < 2) B ON A.gio = B.dist_gio
)
-- # 중복된 tiv_2015와 고유한 위,경도가 있는 행의 tiv_2016을 더함
SELECT ROUND(SUM(tiv_2016),2) as tiv_2016
FROM T3 A
  INNER JOIN T1 B ON A.tiv_2015 = B.tiv_2015