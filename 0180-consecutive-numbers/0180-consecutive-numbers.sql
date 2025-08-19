# Write your MySQL query statement below
select 
    distinct l1.num as ConsecutiveNums
from
    logs l1
inner join
    logs l2
inner join 
    logs l3
on 
    l1.num = l2.num and
    l2.num = l3.num
where
    l1.id = l2.id+1 and
    l1.id = l3.id+2