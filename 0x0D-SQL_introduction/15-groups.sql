-- Lists the no of records with the same score in second_table
-- Result should display: score, number of records for this score with the lable number
-- List sorted by the number of records (Descending)
-- DB passed as args
SELECT SCORE, COUNT(*) AS NUMBER FROM second_table GROUP BY SCORE ORDER BY NUMBER DESC;
