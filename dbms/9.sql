-- Create table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

INSERT INTO Students (StudentID, FirstName, LastName, DepartmentID)
VALUES
    (1, 'John', 'Doe', 1),
    (2, 'Jane', 'Smith', 2),
    (3, 'Michael', 'Johnson', 1),
    (4, 'Emily', 'Williams', 2),
    (5, 'David', 'Brown', 3);

INSERT INTO Departments (DepartmentID, DepartmentName)
VALUES
    (1, 'CSE'),
    (2, 'IT'),
    (3, 'ENTC');

-- Inner Join
-- This type of JOIN returns rows from all tables in which the join condition is true.
SELECT Students.FirstName, Students.LastName, Departments.DepartmentID
FROM Students
INNER JOIN Departments
ON Students.DepartmentID = Departments.DepartmentID;

-- Full Outer Join
-- This type of join returns all rows from both tables with NULL values where the JOIN condition
-- is not true.
SELECT Students.FirstName, Students.LastName, Departments.DepartmentName
FROM Students
FULL OUTER JOIN Departments
ON Students.DepartmentID = Departments.DepartmentID;

-- Left Outer Join
-- This type of join will return all rows from the left-hand table plus records in the right-hand table
-- with matching values.
SELECT
    Students.FirstName,
    Students.LastName,
    Departments.DepartmentName
FROM
    Students
LEFT OUTER JOIN
    Departments ON Students.DepartmentID = Departments.DepartmentID;

-- Right Outer Join
-- This type of join returns all rows from the right-hand table and only those with matching values
-- in the left-hand table.
SELECT
    Students.FirstName,
    Students.LastName,
    Departments.DepartmentName
FROM
    Students
RIGHT OUTER JOIN
    Departments ON Students.DepartmentID = Departments.DepartmentID;