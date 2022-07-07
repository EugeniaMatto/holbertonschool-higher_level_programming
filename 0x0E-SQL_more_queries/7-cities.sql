-- script that creates the database hbtn_0d_usa and the table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE
	, FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id), name VARCHAR(256) NOT NULL)
