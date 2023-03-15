-- This script will create a user `user_0d_1`
-- User will have all privileges
-- User password is 'user_0d_1_pwd'
-- Script should not fail if user already exists

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

