--script that prepares a MySQL server for the project
-- Creates a database called hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user with a password
CREATE USER IF NOT EXISTS 'hbnb_dev@localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Gives the user all privileges to database
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev@localhost';
-- Gives select privileges to user on performance schema
GRANT SELECT PRIVILEGES ON performance_schema TO 'hbnb_dev@localhost';
