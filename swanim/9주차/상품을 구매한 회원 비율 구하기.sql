select year(b.sales_date) as YEAR, month(b.sales_date) as MONTH, count(distinct a.user_id) as PUCHASED_USERS, round(count(distinct a.user_id) / (select count(*) from user_info where year(joined) = '2021') ,1) as PUCHASED_RATIO
from user_info a
join online_sale b on a.user_id = b.user_id
where year(a.joined) = '2021'
group by YEAR, MONTH
order by YEAR, MONTH