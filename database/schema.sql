DROP DATABASE IF EXISTS store_rating_system;
CREATE DATABASE store_rating_system;
USE store_rating_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    address VARCHAR(400) NOT NULL,
    role ENUM('ADMIN','USER','OWNER') NOT NULL
);

CREATE TABLE stores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    address VARCHAR(400) NOT NULL,
    owner_id INT UNIQUE,
    FOREIGN KEY (owner_id) REFERENCES users(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE ratings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    user_id INT NOT NULL,
    store_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,
    FOREIGN KEY (store_id) REFERENCES stores(id)
        ON DELETE CASCADE,
    UNIQUE(user_id, store_id)
);