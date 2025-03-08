# Write your MySQL query statement below
select 
    name as customers
from Customers 
where 1=1
    and id not in (
        select 
            customerId 
        from Orders
    );