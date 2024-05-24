-- Create DB : hbtn_0d_usa; table : cities in hbtn_0d_usa
-- cities -> id INT UNIQUE AUTO_INCREMENT, NOT NULL, PRIMARY KEY; name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256), UNIQUE(id), FOREIGN KEY (state_id) REFERENCES states(id));
