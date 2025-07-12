# Write your MySQL query statement below
SELECT 
    distinct e.num ConsecutiveNums
From
    logs e CROSS JOIN logs l
where l.id - e.id between 0 and 2 and e.num = l.num
group by e.id
having count(*) = 3