-- Active: 1784396333819@@mysql-5fdb1a0-chandananlchandana-2388.j.aivencloud.com@21645@defaultdb
USE defaultdb;

SELECT DATABASE();

SHOW TABLES;

CREATE TABLE test (
    id INT PRIMARY KEY
);

SHOW TABLES;

DROP TABLE test;
INSERT INTO users (name,email,password,address,role)
VALUES
(
'Admin',
'admin@example.com',
'scrypt:32768:8:1$11kybZSKQEmLcFCA$3eb8018fe02a5ae00494bd98bf3788a9697ad08ef58e2e52eb87320cf84c2f9bcb78dea752fb6d59e2c7a45eb35a7bd7fca87e86befdbcb066c0e32401aa457e',
'Bangalore',
'ADMIN'
);

SELECT * FROM users;