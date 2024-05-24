-- List all cities of California that can be found in database hbtn_0d_usa
-- states table : contains only one record where name = California (bud id can be different)
-- Results : sorted in ascending order by cities.id
-- DO NOT use JOIN
-- DB passed as args
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = "Carlifornia") ORDER BY id;
