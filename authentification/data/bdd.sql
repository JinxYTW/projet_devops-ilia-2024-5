CREATE DATABASE IF NOT EXISTS polytex;
USE polytex;

DROP table IF EXISTS users;

CREATE TABLE users (
    username VARCHAR(50) NOT NULL PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    pseudo VARCHAR(50) NOT NULL
);

INSERT INTO users (last_name, first_name, email, password, username, pseudo)
VALUES
    ('Dupont', 'Jean', 'jean.dupont@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'jdupont', 'JeanD'),
    ('Martin', 'Sophie', 'sophie.martin@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'smartin', 'SophieM'),
