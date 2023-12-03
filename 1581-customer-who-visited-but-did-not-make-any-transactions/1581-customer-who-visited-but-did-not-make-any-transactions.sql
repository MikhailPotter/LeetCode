# Write your MySQL query statement below
select
    customer_id
    , count(*) as count_no_trans 
from Visits
left join Transactions
    using (visit_id)
where 1=1
    and amount is null
group by 1