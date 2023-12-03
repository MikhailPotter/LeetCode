# Write your MySQL query statement below
select 
    name
    , sum(amount) as balance
from Transactions 
join Users 
    using (account)
where 1=1
group by 1
having sum(amount) > 10000