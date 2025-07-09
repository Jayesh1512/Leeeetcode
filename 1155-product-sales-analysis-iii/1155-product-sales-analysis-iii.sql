
select 
    product_id,
    year as first_year,
    quantity,
    price
from 
    sales
where (product_id,year) in 
    (select
        product_id,min(s1.year)   
    from 
        sales s1
    group by
        s1.product_id)
