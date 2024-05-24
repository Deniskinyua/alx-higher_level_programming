-- Lists all cities in hbtn_0d_usa
-- Each record should display cities.id, cities.name, states.name;
-- Sorted in ASC by cities.id
-- CAN ONLY use one SELECT statement
-- DB passed as args
SELECT cities.id, cities.name, sts.name FROM cities INNER JOIN states AS sts ON cities.state_id = sts.id ORDER BY cities.id;
