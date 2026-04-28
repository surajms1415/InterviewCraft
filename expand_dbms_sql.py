import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sql_topics = [
        {
            "id": "sql-select",
            "title": "SELECT - Retrieving Data",
            "description": "SELECT is the most fundamental SQL command used to retrieve data from one or more tables.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Syntax & Key Clauses",
                    "content": "**Syntax:** `SELECT column1, column2 FROM table_name WHERE condition;`\n\n**Key Clauses:**\n• **SELECT:** Specifies which columns to retrieve\n• **FROM:** Specifies the table(s) to query\n• **WHERE:** Filters rows based on conditions\n• **DISTINCT:** Removes duplicate rows\n• **AS:** Creates column aliases\n• **LIMIT/TOP:** Restricts number of rows returned"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Select specific columns & conditions\nSELECT name, department FROM Employees WHERE salary > 50000;\n\n-- Using DISTINCT & aliases\nSELECT DISTINCT department FROM Employees;\nSELECT name AS employee_name, salary * 12 AS annual_salary FROM Employees;\n\n-- Multiple conditions with BETWEEN and IN\nSELECT * FROM Employees WHERE department = 'IT' AND salary > 60000;\nSELECT * FROM Products WHERE price BETWEEN 100 AND 500;\nSELECT * FROM Employees WHERE department IN ('IT', 'HR', 'Sales');\n\n-- LIKE for pattern matching\nSELECT * FROM Employees WHERE name LIKE 'J%';     -- Starts with J\nSELECT * FROM Employees WHERE email LIKE '%@gmail.com';  -- Ends with\nSELECT * FROM Employees WHERE name LIKE '_ohn';   -- Second char onwards is 'ohn'\n\n-- ORDER BY and LIMIT\nSELECT * FROM Employees ORDER BY department ASC, salary DESC;\nSELECT * FROM Employees ORDER BY salary DESC LIMIT 10;</pre>"
                }
            ]
        },
        {
            "id": "sql-insert",
            "title": "INSERT - Adding Data",
            "description": "INSERT statement adds new rows to a table.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Syntax & Key Points",
                    "content": "**Syntax:** `INSERT INTO table_name (columns) VALUES (values);`\n\n**Key Points:**\n• Can insert single or multiple rows\n• Column order must match value order\n• Can omit column names if providing all values\n• Can insert from another table using SELECT\n• Auto-increment columns can be omitted"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Insert with specified columns\nINSERT INTO Employees (name, department, salary) VALUES ('Jane Smith', 'HR', 65000);\n\n-- Insert multiple rows\nINSERT INTO Employees (name, department, salary) VALUES\n('Alice Brown', 'IT', 80000),\n('Bob Wilson', 'Sales', 55000),\n('Carol Davis', 'HR', 60000);\n\n-- Insert from another table\nINSERT INTO EmployeeBackup (name, department, salary)\nSELECT name, department, salary FROM Employees WHERE department = 'IT';\n\n-- Insert and get the auto-generated ID (MySQL)\nINSERT INTO Orders (customer_id, total) VALUES (5, 150.00);\nSELECT LAST_INSERT_ID();</pre>"
                }
            ]
        },
        {
            "id": "sql-update",
            "title": "UPDATE - Modifying Data",
            "description": "UPDATE statement modifies existing rows in a table.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Syntax & Key Points",
                    "content": "**Syntax:** `UPDATE table_name SET column1 = value1 WHERE condition;`\n\n**Key Points:**\n• Always use `WHERE` clause (unless updating all rows intentionally)\n• Can update multiple columns in one statement\n• Can use subqueries for values\n• **Be careful:** Without WHERE, ALL rows are updated!"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Update multiple columns\nUPDATE Employees SET salary = 85000, department = 'Senior IT' WHERE emp_id = 101;\n\n-- Update with calculation\nUPDATE Products SET price = price * 1.10;  -- 10% price increase\n\n-- Update using CASE\nUPDATE Employees SET salary = \n    CASE \n        WHEN department = 'IT' THEN salary * 1.15\n        WHEN department = 'HR' THEN salary * 1.10\n        ELSE salary * 1.05\n    END;\n\n-- Update with subquery\nUPDATE Employees \nSET salary = (SELECT AVG(salary) FROM Employees WHERE department = 'IT')\nWHERE emp_id = 102;</pre>"
                }
            ]
        },
        {
            "id": "sql-delete",
            "title": "DELETE - Removing Data",
            "description": "DELETE statement removes rows from a table.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Syntax & Key Points",
                    "content": "**Syntax:** `DELETE FROM table_name WHERE condition;`\n\n**Key Points:**\n• Always use `WHERE` clause (unless deleting all rows)\n• `DELETE` removes rows, `TRUNCATE` removes all rows faster\n• Can use subqueries in WHERE clause\n• Triggers fire on DELETE but not on TRUNCATE\n• DELETE can be rolled back, TRUNCATE often cannot"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Delete specific rows with conditions\nDELETE FROM Orders WHERE status = 'Cancelled' AND order_date < '2024-01-01';\n\n-- Delete using subquery\nDELETE FROM Employees \nWHERE dept_id IN (SELECT dept_id FROM Departments WHERE status = 'Closed');\n\n-- Delete with JOIN (MySQL)\nDELETE e FROM Employees e\nJOIN Departments d ON e.dept_id = d.dept_id\nWHERE d.dept_name = 'Obsolete';\n\n-- TRUNCATE all rows (faster, minimal logging)\nTRUNCATE TABLE TempTable;</pre>"
                }
            ]
        },
        {
            "id": "sql-joins",
            "title": "JOINs - Combining Tables",
            "description": "JOIN combines rows from two or more tables based on related columns.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Types of JOINs",
                    "content": "• **INNER JOIN:** Returns only matching rows from both tables\n• **LEFT JOIN:** All rows from left + matching from right (NULL if no match)\n• **RIGHT JOIN:** All rows from right + matching from left (NULL if no match)\n• **FULL OUTER JOIN:** All rows from both tables\n• **CROSS JOIN:** Cartesian product (every row with every row)\n• **SELF JOIN:** Table joined with itself"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- INNER JOIN (only matching rows)\nSELECT e.name, d.dept_name FROM Employees e\nINNER JOIN Departments d ON e.dept_id = d.dept_id;\n\n-- LEFT JOIN (all employees, even without department)\nSELECT e.name, d.dept_name FROM Employees e\nLEFT JOIN Departments d ON e.dept_id = d.dept_id;\n\n-- SELF JOIN (find employees and their managers)\nSELECT e.name AS employee, m.name AS manager FROM Employees e\nLEFT JOIN Employees m ON e.manager_id = m.emp_id;\n\n-- Multiple JOINs with WHERE\nSELECT e.name, d.dept_name, p.project_name FROM Employees e\nJOIN Departments d ON e.dept_id = d.dept_id\nJOIN Projects p ON e.project_id = p.project_id\nWHERE d.dept_name = 'IT' AND e.salary > 50000;</pre>"
                }
            ]
        },
        {
            "id": "sql-aggregation",
            "title": "Aggregation Functions",
            "description": "Aggregate functions perform calculations on a set of values and return a single value.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Common Functions & Clauses",
                    "content": "**Functions:**\n• `COUNT()`: Number of rows\n• `SUM()`: Total of numeric column\n• `AVG()`: Average value\n• `MIN()`/`MAX()`: Smallest/Largest value\n• `GROUP_CONCAT()` / `STRING_AGG()`: Concatenate values\n\n**Clauses:**\n• `GROUP BY`: Groups rows with same values\n• `HAVING`: Filters groups (like WHERE for aggregates)"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Basic & COUNT variations\nSELECT COUNT(*) FROM Employees;           -- All rows including NULL\nSELECT COUNT(DISTINCT department) FROM Employees;  -- Unique values\n\n-- GROUP BY multiple columns\nSELECT department, job_title, AVG(salary) FROM Employees\nGROUP BY department, job_title;\n\n-- WHERE vs HAVING\nSELECT department, AVG(salary) FROM Employees\nWHERE status = 'Active'      -- Filters rows BEFORE grouping\nGROUP BY department\nHAVING AVG(salary) > 50000;  -- Filters groups AFTER grouping\n\n-- Concatenate values (MySQL)\nSELECT department, GROUP_CONCAT(name ORDER BY name SEPARATOR ', ')\nFROM Employees GROUP BY department;</pre>"
                }
            ]
        },
        {
            "id": "sql-subqueries",
            "title": "Subqueries",
            "description": "A subquery is a query nested inside another query. Can be used in SELECT, FROM, WHERE, or HAVING.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Types & Operators",
                    "content": "**Types:**\n• **Scalar Subquery:** Returns single value\n• **Row Subquery:** Returns single row\n• **Table Subquery:** Returns table (used in FROM)\n• **Correlated Subquery:** References outer query (runs for each outer row)\n\n**Key Operators:** `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, `ANY`, `ALL`"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Scalar subquery in SELECT\nSELECT name, salary, (SELECT AVG(salary) FROM Employees) AS company_avg\nFROM Employees;\n\n-- EXISTS / NOT EXISTS\nSELECT * FROM Departments d\nWHERE EXISTS (SELECT 1 FROM Employees e WHERE e.dept_id = d.dept_id);\n\n-- Correlated subquery (runs for each row)\nSELECT e.name, e.salary FROM Employees e\nWHERE e.salary > (\n    SELECT AVG(salary) FROM Employees WHERE dept_id = e.dept_id\n);\n\n-- Subquery in FROM (derived table)\nSELECT dept_summary.department, dept_summary.avg_sal FROM (\n    SELECT department, AVG(salary) AS avg_sal FROM Employees GROUP BY department\n) AS dept_summary WHERE dept_summary.avg_sal > 60000;</pre>"
                }
            ]
        },
        {
            "id": "sql-window-functions",
            "title": "Window Functions",
            "description": "Window functions perform calculations across a set of rows related to the current row, without collapsing rows like GROUP BY.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Components & Common Functions",
                    "content": "**Components:**\n• `OVER()`: Defines the window\n• `PARTITION BY`: Divides rows into groups\n• `ORDER BY`: Defines order within partition\n• `ROWS/RANGE`: Defines frame boundaries\n\n**Common Functions:**\n• `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`\n• `LEAD()`, `LAG()`: Access next/previous rows\n• `FIRST_VALUE()`, `LAST_VALUE()`\n• aggregates with `OVER()`"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- ROW_NUMBER with PARTITION\nSELECT name, department, salary,\n    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank\nFROM Employees;\n\n-- RANK vs DENSE_RANK\nSELECT name, salary,\n    RANK() OVER (ORDER BY salary DESC) AS rank,        -- 1,2,2,4 (gaps)\n    DENSE_RANK() OVER (ORDER BY salary DESC) AS d_rank -- 1,2,2,3 (no gaps)\nFROM Employees;\n\n-- LAG and LEAD (access adjacent rows)\nSELECT name, salary,\n    LAG(salary, 1) OVER (ORDER BY emp_id) AS prev_salary,\n    LEAD(salary, 1) OVER (ORDER BY emp_id) AS next_salary\nFROM Employees;\n\n-- Running total\nSELECT name, salary, SUM(salary) OVER (ORDER BY emp_id) AS running_total\nFROM Employees;</pre>"
                }
            ]
        },
        {
            "id": "sql-ddl",
            "title": "DDL - Data Definition Language",
            "description": "DDL commands define and modify database structure.",
            "cards": [
                {
                    "type": "list",
                    "heading": "Commands & Constraints",
                    "content": "**Commands:**\n• `CREATE`: Create new objects\n• `ALTER`: Modify existing objects\n• `DROP`: Delete objects\n• `TRUNCATE`: Remove all data from table\n\n**Constraints:**\n• `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- CREATE TABLE with constraints\nCREATE TABLE Employees (\n    emp_id INT PRIMARY KEY AUTO_INCREMENT,\n    name VARCHAR(100) NOT NULL,\n    email VARCHAR(100) UNIQUE,\n    department VARCHAR(50) DEFAULT 'General',\n    salary DECIMAL(10,2) CHECK (salary > 0),\n    manager_id INT,\n    FOREIGN KEY (manager_id) REFERENCES Employees(emp_id)\n);\n\n-- ALTER TABLE operations\nALTER TABLE Employees ADD phone VARCHAR(15);\nALTER TABLE Employees MODIFY COLUMN phone VARCHAR(20);\nALTER TABLE Employees ADD CONSTRAINT chk_salary CHECK (salary >= 0);\n\n-- CREATE INDEX\nCREATE INDEX idx_department ON Employees(department);\n\n-- DROP vs TRUNCATE vs DELETE\n-- DROP: Removes table + data + structure\n-- TRUNCATE: Removes all data, keeps structure\n-- DELETE: Removes specific rows, can use WHERE</pre>"
                }
            ]
        },
        {
            "id": "sql-cte-advanced",
            "title": "CTEs and Advanced SQL",
            "description": "Common Table Expressions (CTEs) create temporary named result sets that simplify complex queries.",
            "cards": [
                {
                    "type": "list",
                    "heading": "CTE Benefits & Advanced Features",
                    "content": "**CTE Benefits:**\n• Improve readability\n• Enable recursive queries\n• Can be referenced multiple times\n• Better than subqueries for complex logic\n\n**Other Advanced Features:**\n• `CASE WHEN`: Conditional logic\n• `COALESCE`/`NULLIF`: NULL handling\n• `UNION`/`INTERSECT`/`EXCEPT`: Set operations"
                },
                {
                    "type": "text",
                    "heading": "SQL Examples",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Simple CTE\nWITH DeptSalary AS (\n    SELECT department, AVG(salary) AS avg_salary FROM Employees GROUP BY department\n)\nSELECT e.name, e.salary, ds.avg_salary FROM Employees e\nJOIN DeptSalary ds ON e.department = ds.department\nWHERE e.salary > ds.avg_salary;\n\n-- CASE WHEN\nSELECT name, salary,\n    CASE \n        WHEN salary >= 100000 THEN 'Senior'\n        WHEN salary >= 60000 THEN 'Mid-level'\n        ELSE 'Junior'\n    END AS level\nFROM Employees;\n\n-- COALESCE (first non-NULL value)\nSELECT name, COALESCE(phone, email, 'No contact') AS contact FROM Employees;\n\n-- UNION (combine results, remove duplicates)\nSELECT name, 'Employee' AS type FROM Employees\nUNION\nSELECT name, 'Customer' AS type FROM Customers;</pre>"
                }
            ]
        }
    ]

    data["dbms"]["topics"].extend(sql_topics)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Successfully injected all SQL topics into DBMS!")
except Exception as e:
    print(f"Error: {e}")
