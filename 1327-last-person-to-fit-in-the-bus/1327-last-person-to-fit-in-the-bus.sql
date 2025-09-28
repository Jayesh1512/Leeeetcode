select q.person_name
from queue q
join (
    select max(turn) as max_turn
    from (
        select
            sum(weight) over (
                order by turn
                rows between unbounded preceding and current row
            ) as csum,
            turn
        from queue
    ) t
    where csum <= 1000
) m
on q.turn = m.max_turn;
