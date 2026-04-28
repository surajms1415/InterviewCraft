import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    dbms_topics = [
        {
            "id": "what-is-dbms",
            "title": "What is DBMS?",
            "description": "A Database Management System (DBMS) is software that enables users to create, manage, and manipulate databases efficiently.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Introduction & Key Components",
                    "content": "A Database Management System (DBMS) acts as an interface between the database and end users or application programs.\n\n**Key Components:**\n• **Database Engine:** Core service for storing and retrieving data\n• **Database Schema:** Logical structure defining organization of data\n• **Query Processor:** Interprets and executes database queries\n• **Transaction Manager:** Ensures ACID properties\n• **Storage Manager:** Manages physical storage of data"
                },
                {
                    "type": "text",
                    "heading": "Types of DBMS",
                    "content": "• **Hierarchical DBMS:** Data organized in tree structure (parent-child)\n• **Network DBMS:** More flexible, allows many-to-many relationships\n• **Relational DBMS (RDBMS):** Data in tables with rows and columns (MySQL, PostgreSQL, Oracle)\n• **Object-oriented DBMS:** Stores data as objects\n• **NoSQL DBMS:** Non-relational, for unstructured data (MongoDB, Cassandra)"
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- RDBMS Example: Creating a simple database structure\nCREATE DATABASE CompanyDB;\nUSE CompanyDB;\n\nCREATE TABLE Employees (\n    emp_id INT PRIMARY KEY,\n    name VARCHAR(100),\n    department VARCHAR(50),\n    salary DECIMAL(10,2)\n);</pre>"
                }
            ]
        },
        {
            "id": "dbms-vs-file-system",
            "title": "DBMS vs File System",
            "description": "File System stores data in files without any relationship management, while DBMS provides structured storage.",
            "cards": [
                {
                    "type": "text",
                    "heading": "File System Limitations",
                    "content": "• **Data Redundancy:** Same data stored multiple times\n• **Data Inconsistency:** Updates may not reflect everywhere\n• **Difficulty in Accessing Data:** No query language\n• **Data Isolation:** Data scattered in various files\n• **Integrity Problems:** No constraint enforcement\n• **Atomicity Issues:** No transaction support\n• **Concurrent Access Anomalies:** No concurrency control\n• **Security Problems:** Limited access control"
                },
                {
                    "type": "text",
                    "heading": "DBMS Advantages",
                    "content": "• **Reduced Redundancy:** Normalization eliminates duplicate data\n• **Data Consistency:** Single source of truth\n• **Easy Data Access:** SQL queries for complex retrieval\n• **Data Integrity:** Constraints ensure valid data\n• **Atomicity:** Transactions are all-or-nothing\n• **Concurrent Access:** Multiple users safely\n• **Security:** Role-based access control\n• **Backup & Recovery:** Built-in mechanisms"
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- File System Problem:\n-- students.txt: John, CS, john@email.com\n-- grades.txt: John, CS, A+\n-- If John changes email, must update multiple files!\n\n-- DBMS Solution:\nCREATE TABLE Students (\n    student_id INT PRIMARY KEY,\n    name VARCHAR(100),\n    email VARCHAR(100) UNIQUE\n);\n\nCREATE TABLE Grades (\n    student_id INT,\n    course VARCHAR(50),\n    grade CHAR(2),\n    FOREIGN KEY (student_id) REFERENCES Students(student_id)\n);\n\n-- Email change only needs ONE update!\nUPDATE Students SET email = 'new@email.com' WHERE student_id = 1;</pre>"
                }
            ]
        },
        {
            "id": "acid-properties",
            "title": "ACID Properties",
            "description": "ACID properties ensure reliable database transactions. Every transaction must satisfy these four properties.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Atomicity (All or Nothing)",
                    "content": "• Transaction is treated as single unit\n• Either all operations complete successfully, or none do\n• If any operation fails, entire transaction is rolled back\n• **Example:** Bank transfer - debit AND credit must both happen"
                },
                {
                    "type": "text",
                    "heading": "Consistency (Valid State)",
                    "content": "• Database must be in valid state before and after transaction\n• All constraints, triggers, and rules must be satisfied\n• Data integrity is maintained\n• **Example:** Account balance cannot be negative"
                },
                {
                    "type": "text",
                    "heading": "Isolation (Independent Execution)",
                    "content": "• Concurrent transactions don't interfere with each other\n• Each transaction appears to run in isolation\n• Intermediate states are not visible to other transactions\n• Prevents dirty reads, non-repeatable reads, phantom reads"
                },
                {
                    "type": "text",
                    "heading": "Durability (Permanent Changes)",
                    "content": "• Once transaction is committed, changes are permanent\n• Survives system crashes, power failures\n• Achieved through write-ahead logging (WAL)"
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Bank Transfer Example: $500 from Account A to B\n\n-- Without ACID (dangerous):\nUPDATE Accounts SET balance = balance - 500 WHERE account = 'A';\n-- System crashes here! Money disappeared!\nUPDATE Accounts SET balance = balance + 500 WHERE account = 'B';\n\n-- With ACID (safe):\nSTART TRANSACTION;\n\nUPDATE Accounts SET balance = balance - 500 WHERE account = 'A';\nUPDATE Accounts SET balance = balance + 500 WHERE account = 'B';\n\n-- If both succeed:\nCOMMIT;  -- Changes are permanent (Durability)\n\n-- If any fails:\nROLLBACK;  -- All changes undone (Atomicity)</pre>"
                }
            ]
        },
        {
            "id": "keys-in-dbms",
            "title": "Keys in DBMS",
            "description": "Keys are attributes used to uniquely identify records and establish relationships between tables.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Super Key & Candidate Key",
                    "content": "**Super Key:**\n• Any set of attributes that uniquely identifies a row\n• May contain extra attributes not needed for uniqueness\n• Example: `{emp_id}`, `{emp_id, name}`, `{emp_id, name, dept}`\n\n**Candidate Key:**\n• Minimal super key (no redundant attributes)\n• A table can have multiple candidate keys\n• Example: `{emp_id}`, `{email}`, `{phone}` - all unique"
                },
                {
                    "type": "text",
                    "heading": "Primary, Foreign, Alternate & Composite Keys",
                    "content": "**Primary Key:** Chosen candidate key to uniquely identify records. Cannot be NULL, must be unique. Only ONE primary key per table. Creates clustered index by default.\n\n**Foreign Key:** References primary key in another table. Establishes relationships. Can be NULL. Maintains referential integrity.\n\n**Alternate Key:** Candidate keys not chosen as primary key.\n\n**Composite Key:** Primary key made of multiple columns. Used when single column can't ensure uniqueness."
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>CREATE TABLE Employees (\n    emp_id INT PRIMARY KEY,           -- Primary Key\n    email VARCHAR(100) UNIQUE,        -- Candidate/Alternate Key\n    phone VARCHAR(15) UNIQUE,         -- Candidate/Alternate Key\n    name VARCHAR(100),\n    dept_id INT,\n    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)\n);\n\n-- Composite Key Example\nCREATE TABLE OrderItems (\n    order_id INT,\n    product_id INT,\n    quantity INT,\n    PRIMARY KEY (order_id, product_id)  -- Composite Key\n);</pre>"
                }
            ]
        },
        {
            "id": "normalization",
            "title": "Normalization",
            "description": "Normalization is the process of organizing data to reduce redundancy and improve data integrity.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Normal Forms (1NF & 2NF)",
                    "content": "**First Normal Form (1NF):**\n• Each cell contains atomic (single) values\n• No repeating groups or arrays\n• Each record is unique\n\n**Second Normal Form (2NF):**\n• Must be in 1NF\n• No partial dependencies\n• All non-key attributes fully depend on entire primary key\n• Relevant only for composite primary keys"
                },
                {
                    "type": "text",
                    "heading": "Normal Forms (3NF & BCNF)",
                    "content": "**Third Normal Form (3NF):**\n• Must be in 2NF\n• No transitive dependencies\n• Non-key attributes depend only on primary key, not on other non-key attributes\n\n**Boyce-Codd Normal Form (BCNF):**\n• Stronger version of 3NF\n• Every determinant must be a candidate key\n\n**When to Denormalize:**\n• Read-heavy applications needing faster queries\n• Reporting and analytics databases\n• When joins become too expensive"
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- UNNORMALIZED (violates 1NF):\n-- Student | Courses\n-- John    | Math, Science, English  ← Multiple values!\n\n-- 1NF: Atomic values\nCREATE TABLE StudentCourses (student_id INT, student_name VARCHAR(100), course VARCHAR(50), instructor VARCHAR(100), instructor_dept VARCHAR(50));\n\n-- 2NF: Remove partial dependencies\nCREATE TABLE Students (student_id INT PRIMARY KEY, name VARCHAR(100));\nCREATE TABLE Courses (course_id INT PRIMARY KEY, course_name VARCHAR(50), instructor VARCHAR(100), instructor_dept VARCHAR(50));\nCREATE TABLE Enrollments (student_id INT, course_id INT, PRIMARY KEY (student_id, course_id));\n\n-- 3NF: Remove transitive dependencies\nCREATE TABLE Instructors (instructor_id INT PRIMARY KEY, name VARCHAR(100), dept VARCHAR(50));\nCREATE TABLE Courses_3NF (course_id INT PRIMARY KEY, course_name VARCHAR(50), instructor_id INT);</pre>"
                }
            ]
        },
        {
            "id": "er-diagrams",
            "title": "ER Diagrams",
            "description": "Entity-Relationship (ER) Diagrams visually represent database structure showing entities, attributes, and relationships.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Entities & Attributes",
                    "content": "**Entities:**\n• Real-world objects represented in database (Rectangles)\n• Strong Entity: Has its own primary key\n• Weak Entity: Depends on another entity for identification\n\n**Attributes:**\n• Properties of entities (Ovals)\n• Types: Simple, Composite, Derived, Multi-valued, Key"
                },
                {
                    "type": "text",
                    "heading": "Relationships, Cardinality & Participation",
                    "content": "**Relationships:** Associations between entities (Diamonds)\n\n**Cardinality:**\n• 1:1 - One employee has one passport\n• 1:N - One department has many employees\n• M:N - Many students enroll in many courses\n\n**Participation:**\n• Total (mandatory): Every entity must participate\n• Partial (optional): Entity may or may not participate"
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- ER Diagram to Tables Conversion\n-- Entity: Student\nCREATE TABLE Student (student_id INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100));\n\n-- Entity: Course\nCREATE TABLE Course (course_id INT PRIMARY KEY, title VARCHAR(100), credits INT);\n\n-- Relationship: Enrolls (M:N creates junction table)\nCREATE TABLE Enrolls (\n    student_id INT, course_id INT, enrollment_date DATE, grade CHAR(2),\n    PRIMARY KEY (student_id, course_id),\n    FOREIGN KEY (student_id) REFERENCES Student(student_id),\n    FOREIGN KEY (course_id) REFERENCES Course(course_id)\n);\n\n-- Weak Entity: Dependent (depends on Employee)\nCREATE TABLE Dependent (\n    emp_id INT, dependent_name VARCHAR(100),\n    PRIMARY KEY (emp_id, dependent_name),\n    FOREIGN KEY (emp_id) REFERENCES Employee(emp_id)\n);</pre>"
                }
            ]
        },
        {
            "id": "transactions",
            "title": "Transactions",
            "description": "A transaction is a logical unit of work containing one or more database operations that must be executed as a whole.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Transaction States & Control Commands",
                    "content": "**States:**\n• Active: Transaction is being executed\n• Partially Committed: Final statement executed, awaiting commit\n• Committed: Successfully completed, changes permanent\n• Failed: Error occurred, cannot proceed\n• Aborted: Rolled back\n\n**Control Commands:**\n• BEGIN/START TRANSACTION: Start new transaction\n• COMMIT: Save all changes permanently\n• ROLLBACK: Undo all changes since last commit\n• SAVEPOINT: Create checkpoint within transaction"
                },
                {
                    "type": "text",
                    "heading": "Concurrency Problems & Isolation Levels",
                    "content": "**Concurrency Problems:**\n• Dirty Read: Reading uncommitted data\n• Non-Repeatable Read: Same query returns different results\n• Phantom Read: New rows appear in repeated query\n• Lost Update: Two transactions overwrite each other\n\n**Isolation Levels:**\n• READ UNCOMMITTED: Allows dirty reads\n• READ COMMITTED: No dirty reads\n• REPEATABLE READ: No dirty or non-repeatable reads\n• SERIALIZABLE: Highest isolation, no phantoms"
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>START TRANSACTION;\nINSERT INTO Orders (order_id, customer_id, total) VALUES (1001, 5, 500.00);\n\nSAVEPOINT order_created;\n\nINSERT INTO OrderItems (order_id, product_id, qty) VALUES (1001, 101, 2);\nINSERT INTO OrderItems (order_id, product_id, qty) VALUES (1001, 102, 1);\n\n-- Product 102 out of stock!\nROLLBACK TO SAVEPOINT order_created;\n\n-- Try different product\nINSERT INTO OrderItems (order_id, product_id, qty) VALUES (1001, 103, 1);\nCOMMIT;\n\n-- Isolation Level Example\nSET TRANSACTION ISOLATION LEVEL REPEATABLE READ;</pre>"
                }
            ]
        },
        {
            "id": "indexing",
            "title": "Indexing",
            "description": "An index is a data structure that improves the speed of data retrieval operations on a database table.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Why Indexing? & Types",
                    "content": "• **Without index:** Full table scan O(n)\n• **With index:** Quick lookup O(log n) for B-Tree\n• **Trade-off:** Faster reads, slower writes\n\n**Types of Indexes:**\n• Primary Index: On primary key, automatically created\n• Secondary Index: On non-primary key columns\n• Clustered Index: Determines physical order (only one per table)\n• Non-Clustered Index: Separate structure pointing to data\n• Unique Index: Ensures no duplicate values\n• Composite Index: On multiple columns"
                },
                {
                    "type": "text",
                    "heading": "Index Data Structures & When to Use",
                    "content": "**Data Structures:**\n• B-Tree: Balanced tree, good for range queries\n• B+ Tree: All data in leaves, better for range scans\n• Hash Index: O(1) for exact match, no range support\n• Bitmap Index: For low-cardinality columns\n\n**When to Use Indexes:**\n✓ Frequently queried columns (WHERE, JOIN, ORDER BY)\n✓ Foreign key columns\n✗ Small tables\n✗ Frequently updated columns\n✗ Columns with many NULL values"
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>CREATE TABLE Products (\n    product_id INT PRIMARY KEY,  -- Primary index auto-created\n    name VARCHAR(100),\n    category VARCHAR(50),\n    price DECIMAL(10,2)\n);\n\n-- Single column index\nCREATE INDEX idx_category ON Products(category);\n\n-- Composite index (order matters!)\nCREATE INDEX idx_cat_price ON Products(category, price);\n\n-- Unique index\nCREATE UNIQUE INDEX idx_name ON Products(name);\n\n-- Example check\nEXPLAIN SELECT * FROM Products WHERE category = 'Electronics';</pre>"
                }
            ]
        },
        {
            "id": "views",
            "title": "Views",
            "description": "A View is a virtual table based on the result of a SQL query. Simplifies complex queries and adds security.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Benefits & Types",
                    "content": "**Benefits:**\n• Simplify Complex Queries: Hide joins and aggregations\n• Security: Restrict access to specific columns/rows\n• Data Independence: Applications don't need to know underlying structure\n\n**Types of Views:**\n• Simple View: Based on single table, can be updated\n• Complex View: Based on multiple tables, joins, aggregations\n• Materialized View: Physically stores data, needs refresh\n\n**Limitations:** Performance hit since query runs each time (unless materialized), update restrictions, and no indexes allowable mostly."
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Simple view\nCREATE VIEW ActiveEmployees AS\nSELECT emp_id, name, department, salary FROM Employees WHERE status = 'Active';\n\n-- Security view (hide salary)\nCREATE VIEW PublicEmployeeInfo AS\nSELECT emp_id, name, department, email FROM Employees;\nGRANT SELECT ON PublicEmployeeInfo TO hr_staff;\n\n-- Materialized View (PostgreSQL)\nCREATE MATERIALIZED VIEW MonthlySales AS\nSELECT DATE_TRUNC('month', sale_date) as month, SUM(amount) as total\nFROM Sales GROUP BY 1;\nREFRESH MATERIALIZED VIEW MonthlySales;</pre>"
                }
            ]
        },
        {
            "id": "stored-procedures-triggers",
            "title": "Stored Procedures & Triggers",
            "description": "Stored Procedures are precompiled SQL code stored in the database. Triggers are special procedures that automatically execute.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Stored Procedures vs Triggers",
                    "content": "**Stored Procedures Benefits:**\n• Performance: Precompiled, cached execution plans\n• Security: Can grant EXECUTE without table access\n• Reusability: Write once, call from anywhere\n• Reduced Network Traffic: Single call executes multiple statements\n\n**Triggers:**\n• Automatically fire on INSERT, UPDATE, DELETE\n• BEFORE triggers: Validate/modify data before operation\n• AFTER triggers: Audit, cascade operations after change\n• INSTEAD OF triggers: Replace the original operation\n\n**Use Cases:** Audit logging, Enforcing complex business rules, Replicating data."
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Stored Procedure\nDELIMITER //\nCREATE PROCEDURE TransferMoney(IN from_acc INT, IN to_acc INT, IN amount DECIMAL(10,2))\nBEGIN\n    DECLARE bal DECIMAL(10,2);\n    SELECT balance INTO bal FROM Accounts WHERE account_id = from_acc;\n    IF bal >= amount THEN\n        START TRANSACTION;\n        UPDATE Accounts SET balance = balance - amount WHERE account_id = from_acc;\n        UPDATE Accounts SET balance = balance + amount WHERE account_id = to_acc;\n        COMMIT;\n    END IF;\nEND //\nDELIMITER ;\n\n-- Trigger for Audit Log\nCREATE TRIGGER salary_audit\nAFTER UPDATE ON Employees FOR EACH ROW\nBEGIN\n    IF OLD.salary != NEW.salary THEN\n        INSERT INTO EmployeeAudit (emp_id, old_salary, new_salary, changed_at)\n        VALUES (NEW.emp_id, OLD.salary, NEW.salary, NOW());\n    END IF;\nEND;</pre>"
                }
            ]
        },
        {
            "id": "relational-algebra",
            "title": "Relational Algebra",
            "description": "Relational Algebra is a procedural query language that uses operators to manipulate relations (tables) and produce new relations.",
            "cards": [
                {
                    "type": "text",
                    "heading": "Basic & Derived Operations",
                    "content": "**Basic Operations:**\n• Selection (σ): Selects rows satisfying a condition\n• Projection (π): Selects specific columns\n• Union (∪): Combines tuples from two relations\n• Set Difference (−): Tuples in R1 but not in R2\n• Cartesian Product (×): All combinations of tuples from two relations\n\n**Derived Operations:**\n• Intersection (∩): Common tuples in both relations\n• Join (⋈): Combines related tuples from two relations (Natural, Theta, Equi)\n• Division (÷): Used for 'for all' type queries"
                },
                {
                    "type": "text",
                    "heading": "SQL Example",
                    "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Selection (σ): σ(salary > 50000)(Employees)\nSELECT * FROM Employees WHERE salary > 50000;\n\n-- Projection (π): π(name, department)(Employees)\nSELECT name, department FROM Employees;\n\n-- Union (∪): R1 ∪ R2\nSELECT * FROM Employees_2023 UNION SELECT * FROM Employees_2024;\n\n-- Set Difference (−): R1 − R2\nSELECT * FROM AllCustomers EXCEPT SELECT * FROM PremiumCustomers;\n\n-- Natural Join (⋈): Employees ⋈ Departments\nSELECT * FROM Employees NATURAL JOIN Departments;\n\n-- Theta Join: Employees ⋈(e.dept_id = d.dept_id) Departments\nSELECT * FROM Employees e JOIN Departments d ON e.dept_id = d.dept_id;</pre>"
                }
            ]
        }
    ]

    data["dbms"]["topics"] = dbms_topics

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Updated DBMS Topics with Granular SQL examples accurately!")
except Exception as e:
    print(f"Error: {e}")
