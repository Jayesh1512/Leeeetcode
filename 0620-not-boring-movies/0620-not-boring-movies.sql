# Write your MySQL query statement below
select
    id , movie , description , rating
from cinema
where
    description <> 'boring' and
    id % 2 <> 0
order by rating desc