-- Create table1
CREATE TABLE table1 (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Insert data into table1
INSERT INTO table1 (id, name) VALUES
    (1, 'John'),
    (2, 'Jane'),
    (3, 'Bob'),
    (4, 'Alice');

-- Create table2
CREATE TABLE table2 (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Insert data into table2
INSERT INTO table2 (id, name) VALUES
    (3, 'Bob'),
    (4, 'Alice'),
    (5, 'Charlie'),
    (6, 'David');

-- UNION
SELECT id, name FROM table1
UNION
SELECT id, name FROM table2;

-- UNION ALL
SELECT id, name FROM table1
UNION ALL
SELECT id, name FROM table2;

-- INTERSECT
SELECT id, name FROM table1
INTERSECT
SELECT id, name FROM table2;

-- MINUS
SELECT id, name FROM table1
MINUS
SELECT id, name FROM table2;

-- String operations
SELECT CONCAT(name, ' Smith') AS full_name FROM table1;
SELECT LOWER(name) AS lowercase_name FROM table1;
SELECT UPPER(name) AS uppercase_name FROM table1;
SELECT SUBSTRING(name, 1, 2) AS first_two_letters FROM table1;
SELECT LENGTH(name) AS name_length FROM table1;