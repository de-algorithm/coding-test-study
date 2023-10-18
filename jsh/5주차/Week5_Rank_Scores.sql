# Medium
# LTC
# 10min

select a.score, j.rank
from Scores a
left join (
    SELECT score, 
    RANK() OVER (ORDER BY score DESC) as "rank"
    from Scores
    group by score
) j on a.score = j.score
order by a.score desc