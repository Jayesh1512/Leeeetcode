# Write your MySQL query statement below
SELECT product_name , year , price
FROM SALES INNER JOIN PRODUCT
ON SALES.PRODUCT_ID = PRODUCT.PRODUCT_ID