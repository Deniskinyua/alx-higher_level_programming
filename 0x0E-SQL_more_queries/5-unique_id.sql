-- Create table unique_id : id INT DEFAULT 1 & UNIQUE, name VARCHAR(256)
-- DB passed as args
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, name VARCHAR(256), UNIQUE(id));
