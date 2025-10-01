SELECT distinct
    visited_on,
    amount,
    round(amount/7,2) as average_amount
FROM (
    SELECT
        visited_on,
        SUM(amount) over (
            ORDER BY visited_on
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ) as amount
    FROM customer
) t

WHERE
    DATE_SUB(visited_on, INTERVAL 6 DAY) IN (SELECT visited_on FROM customer)
