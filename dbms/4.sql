-- Create the table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20)
);

-- Insert data
INSERT INTO customers (customer_id, first_name, last_name, email, phone)
VALUES
    (1, 'John', 'Doe', 'john.doe@example.com', '123-456-7890'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', '987-654-3210'),
    (3, 'Bob', 'Johnson', 'bob.johnson@example.com', '456-789-0123');

-- Update data
UPDATE customers
SET phone = '555-123-4567'
WHERE customer_id = 2;

-- Delete data
DELETE FROM customers
WHERE customer_id = 3;

-- Select data
SELECT * FROM customers;