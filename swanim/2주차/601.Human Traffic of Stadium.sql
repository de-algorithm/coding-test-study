select distinct s1.*
from stadium s1, stadium s2, stadium s3
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
and(
  (s1.id - s2.id = 1 and s1.id - s3.id = 2 and s2.id - s3.id = 1) or
  (s2.id - s1.id = 1 and s2.id - s3.id = 2 and s1.id - s3.id = 1) or
  (s3.id - s2.id = 1 and s2.id - s1.id = 1 and s3.id - s1.id = 2) 
)
order by s1.visit_date;
