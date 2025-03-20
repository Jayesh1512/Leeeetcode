SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM visits v
LEFT JOIN transactions t
ON v.visit_id = t.visit_id
where transaction_id is NULL
GROUP BY v.customer_id;
