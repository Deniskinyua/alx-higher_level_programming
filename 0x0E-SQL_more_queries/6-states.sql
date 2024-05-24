-- Create DB : hbtn_0d_usa; TABLE : states in hbtn_0d_usa;
-- states -> id INT UNIQUE, AUTO generated, cant be null, PRIMARY KEY, name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256), UNIQUE(id));
