-- This script will create a new db `hbtn_0d_2` and user `user_0d_2`
-- User should have only SELECT privilege in db
-- User password should be set to 'user_0d_2_pwd'
-- Script should not fail if db and user already exists

CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
