-- Creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
name varchar(256) NOT NULL
);
