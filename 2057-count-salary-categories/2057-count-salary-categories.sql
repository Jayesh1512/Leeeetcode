with c as (
    select 'Low Salary' as category
    union all
    select 'Average Salary' as category
    union all
    select 'High Salary' as category
)


select c.category, ifnull(count(m.category),0) as accounts_count
from 

(select 
    case
        when income < 20000 then 'Low Salary'
        when income <= 50000 then 'Average Salary'
        else 'High Salary'
    end as category
from Accounts) as m

right join c on c.category = m.category

group by c.category
