-- On delete Cascade using CREATE TABLE

CREATE TABLE products
( 
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(25)
);

CREATE TABLE inventory
( 
    inventory_id INT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT,
    min_level INT,
    max_level INT,
    CONSTRAINT fk_inv_product_id
    FOREIGN KEY (product_id)
    REFERENCES products (product_id)
    ON DELETE CASCADE
);

--  In this foreign key example, we've created our parent table as the products table.
-- The products table has a primary key that consists of the product_id field.

--  Next, we&#39;ve created a second table called inventory that will be the child table in this
-- foreign key with cascade delete example. We have used the CREATE TABLE statement
-- to create a foreign key on the inventory table called fk_inv_product_id. The foreign key
-- establishes a relationship between the product_id column in the inventory table and
-- the product_id column in the products table.

--  For this foreign key, we have specified the ON DELETE CASCADE clause which tells
-- SQL Server to delete the corresponding records in the child table when the data in the
-- parent table is deleted. So in this example, if a product_id value is deleted from
-- the products table, the corresponding records in the inventory table that use
-- this product_id will also be deleted.

-- On delete Cascade using ALTER TABLE

ALTER TABLE inventory
ADD CONSTRAINT fk_inv_product_id
FOREIGN KEY (product_id)
REFERENCES products (product_id)
ON DELETE CASCADE;

--  In this foreign key example, we&#39;ve created a foreign key on the inventory table
-- called fk_inv_product_id that references the products table based on the product_id field.

--  For this foreign key, we have specified the ON DELETE CASCADE clause which tells
-- SQL Server to delete the corresponding records in the child table when the data in the
-- parent table is deleted. So in this example, if a product_id value is deleted from
-- the products table, the corresponding records in the inventory table that use
-- this product_id will also be deleted.

-- On update Cascade using CREATE TABLE

CREATE TABLE products
( 
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(25)
);

CREATE TABLE inventory
( 
    inventory_id INT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT,
    min_level INT,
    max_level INT,
    CONSTRAINT fk_inv_product_id
    FOREIGN KEY (product_id)
    REFERENCES products (product_id)
    ON UPDATE CASCADE
);

-- On delete SET NULL using CREATE TABLE

CREATE TABLE products
( 
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(25)
);

CREATE TABLE inventory
( 
    inventory_id INT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT,
    min_level INT,
    max_level INT,
    CONSTRAINT fk_inv_product_id
    FOREIGN KEY (product_id)
    REFERENCES products (product_id)
    ON DELETE SET NULL
);