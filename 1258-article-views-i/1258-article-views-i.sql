# Write your MySQL query statement below
SELECT distinct AUTHOR_ID AS id 
FROM VIEWS
WHERE AUTHOR_ID = VIEWER_ID order by author_id;