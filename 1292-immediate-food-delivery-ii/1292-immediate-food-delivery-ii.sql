SELECT
  ROUND(
    100 * SUM(order_date = customer_pref_delivery_date) / COUNT(*),
    2
  ) AS immediate_percentage
FROM
  (
    SELECT *
    FROM Delivery
    WHERE (customer_id, order_date) IN (
      SELECT customer_id, MIN(order_date)
      FROM Delivery
      GROUP BY customer_id
    )
  ) AS first_orders;
