WITH r AS (
    SELECT requester_id, COUNT(*) AS cr
    FROM RequestAccepted
    GROUP BY requester_id
), a AS (
    SELECT accepter_id, COUNT(*) AS ar
    FROM RequestAccepted
    GROUP BY accepter_id
), fmap as(
SELECT 
    COALESCE(r.requester_id, a.accepter_id) AS user_id,
    ifnull(r.cr,0)+ifnull(a.ar,0) as counter
FROM r
LEFT JOIN a ON r.requester_id = a.accepter_id
union
SELECT 
    COALESCE(r.requester_id, a.accepter_id) AS user_id,
    ifnull(r.cr,0)+ifnull(a.ar,0) as counter
FROM r
RIGHT JOIN a ON r.requester_id = a.accepter_id
)

select user_id as id,counter as num
from fmap
where counter = (
    select max(counter) from fmap
)

