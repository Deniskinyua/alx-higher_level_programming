-- Creates a table called first_table in the current database
-- Values: id (INT), name (VARCHAR(256))
-- Database name will be passed as an argument of msql command
-- if table exists should not fail
-- DO NOT use SELECT or SHOW
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
