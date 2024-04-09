-- 많은 평점을 남긴 user name -> greatest_users
-- 2020년 2월 영화 중 평균 평점이 제일 높은 movie_name -> highest_rating
with greatest_users as (
    select u.name results from Users u right join (
        select user_id, count(*) count_rating from MovieRating 
        group by user_id
    ) mr on mr.user_id = u.user_id 
    order by count_rating desc, u.name
    limit 1
),

highest_rating as (
    select m.title results from Movies m 
    right join (
        select movie_id, avg(rating) avg_rating 
        from MovieRating
        where date_format(created_at,'%Y-%m') = '2020-02'
        group by movie_id
        )mr on mr.movie_id = m.movie_id
    order by avg_rating desc, m.title
    limit 1
)

select results from greatest_users 
union all
select results from highest_rating 