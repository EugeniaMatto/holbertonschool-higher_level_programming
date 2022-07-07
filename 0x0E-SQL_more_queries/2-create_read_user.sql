-- SQL
-- command to create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2
-- command to create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- command to give privilege SELECT to user
GRANT SELECT PRIVILEGE ON hbtn_0d_2 TO 'user_0d_2'@'localhost'
