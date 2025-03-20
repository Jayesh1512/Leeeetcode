SELECT W1.ID as Id
FROM Weather W1 , Weather W2
WHERE DATEDIFF(w1.recordDate , w2.recordDate) = 1
AND
W1.TEMPERATURE > W2.TEMPERATURE
;
