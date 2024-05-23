-- Creates a table second_table in database hbtn_0c_0
-- Adds multiple rows: id INT, name VARCHAR(256), score INT;
-- Database passed as an argument
-- If exists, script should not fail;
-- DO NOT use SELECT & SHOW;
-- created records:
-- id = 1, name = "John", score = 10;
-- etc..
CREATE TABLE IF NOT EXISTS second_table (ID INT, NAME VARCHAR(256), SCORE INT);
INSERT INTO second_table (ID, NAME, SCORE) VALUES(1, "John", 10);
INSERT INTO second_table (ID, NAME, SCORE) VALUES(3, "Alex", 3);
INSERT INTO second_table (ID, NAME, SCORE) VALUES(3, "Bob", 14);
INSERT INTO second_table (ID, NAME, SCORE) VALUES(4, "George", 8);




