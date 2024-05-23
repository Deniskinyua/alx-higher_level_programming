-- List all records of second_table
-- DO NOT list rows without a name 
-- Results display: SCORE NAME
-- DB passed as args
SELECT SCORE, NAME FROM second_table WHERE NAME != "" ORDER BY SCORE DESC;
