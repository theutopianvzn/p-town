-- CREATE TABLE
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    hire_date DATE
);

-- INSERT DATA
INSERT INTO employees (employee_id, first_name, last_name, department, hire_date)
VALUES
    (1, 'John', 'Doe', 'Sales', '2020-01-01'),
    (2, 'Jane', 'Smith', 'Marketing', '2021-03-15'),
    (3, 'Bob', 'Johnson', 'IT', '2022-06-30');

-- ALTER TABLE (add column)
ALTER TABLE employees
ADD COLUMN salary DECIMAL(10, 2);

-- UPDATE DATA (set salary)
UPDATE employees
SET salary = 50000.00
WHERE employee_id = 1;

UPDATE employees
SET salary = 60000.00
WHERE employee_id = 2;

UPDATE employees
SET salary = 70000.00
WHERE employee_id = 3;

-- RENAME TABLE
RENAME TABLE employees TO staff;

-- TRUNCATE TABLE
TRUNCATE TABLE staff;

-- DROP TABLE
DROP TABLE staff;