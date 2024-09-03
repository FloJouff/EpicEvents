CREATE DATABASE epic_db;


CREATE TABLE Role (
    role_id INTEGER PRIMARY KEY,
    role VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE User(
    user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(65) NOT NULL,
    firstname VARCHAR(65) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    role_id INTEGER REFERENCES Role(role_id),
    password VARCHAR(255),

);


INSERT INTO `Role` (`role_id`, `role`) 
VALUES 
    ('1', 'GESTION'),
    ('2', 'COMMERCIAL'),
    ('3', 'SUPPORT'),
    ('4', 'ADMIN');

INSERT INTO `User` (`name`, `firstname`, `email`, `role_id`, `password`)
VALUES ('admin', 'admin', '(admin@mail.com)', '4', '$argon2id$v=19$m=65536,t=3,p=4$H/trA+MXh+6KpBCEVdWENw$XI39fFhWL5Vbto2Cjqbb5PclWesR675ziEsfRWeupFg');

