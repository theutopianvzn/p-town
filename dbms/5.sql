-- Create the departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

-- Create the table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    fee DECIMAL(10, 2) DEFAULT 50000.00,
    admission_date DATE NOT NULL,
    teacher_id INT,
    CONSTRAINT check_fee CHECK (fee > 0),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (teacher_id) REFERENCES students(student_id)
);


-- Insert data into departments table
INSERT INTO departments (department_id, department_name)
VALUES (1, 'Sales'), (2, 'Marketing'), (3, 'Engineering');

-- Insert data into students table
INSERT INTO students (student_id, first_name, last_name, email, department_id, fee, admission_date, teacher_id)
VALUES
    (1, 'John', 'Doe', 'john.doe@company.com', 1, 60000.00, '2020-01-01', NULL),
    (2, 'Jane', 'Smith', 'jane.smith@company.com', 2, 55000.00, '2021-03-15', 1),
    (3, 'Bob', 'Johnson', 'bob.johnson@company.com', 1, 65000.00, '2019-06-01', 1),
    (4, 'Alice', 'Williams', 'alice.williams@company.com', 3, 70000.00, '2022-09-01', NULL),
    (5, 'Tom', 'Brown', 'tom.brown@company.com', 3, 62000.00, '2018-11-01', 4);

-- Print all columns from the students table
SELECT * FROM students;

-- Print specific columns from the students table
SELECT student_id, first_name, last_name, email, department_id, fee, admission_date, teacher_id
FROM students;

-- Print columns with aliases
SELECT student_id AS "Student ID", first_name AS "First Name", last_name AS "Last Name", email AS "Email Address", department_id AS "Department", fee AS "fee", admission_date AS "Admission Date", teacher_id AS "Teacher"
FROM students;

-- Print columns from both students and departments tables
SELECT e.student_id, e.first_name, e.last_name, e.email, d.department_name, e.fee, e.admission_date, e.teacher_id
FROM students e
JOIN departments d ON e.department_id = d.department_id;

-- Print columns with a filter
SELECT student_id, first_name, last_name, email, department_id, fee, admission_date, teacher_id
FROM students
WHERE fee > 60000;

-- Print columns with ordering
SELECT student_id, first_name, last_name, email, department_id, fee, admission_date, teacher_id
FROM students
ORDER BY admission_date DESC;