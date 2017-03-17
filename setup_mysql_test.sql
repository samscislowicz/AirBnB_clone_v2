-- a script that prepares a MySQL server for the project
-- Creates a database called hbnb_test_db
CREATE DATABASE IF NOT EXISTS 'hbnb_test_db';
-- Creates a new user called hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test@localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Sets privileges for user
GRANT ALL PRIVILEGES TO 'hbnb_test@localhost' ON 'hbnb_test_db';
GRANT SELECT PRIVILEGES TO 'hbnb_test@localhost' ON 'performance_schema';
