CREATE DATABASE ev_charging;

USE ev_charging;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    vehicle_no VARCHAR(20) UNIQUE
);

CREATE TABLE stations (
    station_id INT AUTO_INCREMENT PRIMARY KEY,
    station_name VARCHAR(100),
    location VARCHAR(255)
);
select * from users;