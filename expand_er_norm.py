import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    er_diagram_topic = {
        "id": "er-diagrams",
        "title": "ER Diagrams",
        "description": "Entity-Relationship (ER) Diagrams visually represent database structure showing entities, attributes, and relationships.",
        "cards": [
            {
                "type": "text",
                "heading": "1. Entities: The 'Nouns' of your System",
                "content": "Entities represent real-world objects or concepts.\n\n• **Strong Entity:** An entity that exists independently of others. It has a Primary Key that uniquely identifies it. (Example: An Employee is strong because they exist regardless of dependents).\n\n• **Weak Entity:** An entity that cannot be uniquely identified by its own attributes alone. It depends on a 'Strong Entity' (Owner). Visual: Drawn as a **Double Rectangle**.\n\n• **Discriminator (Partial Key):** Weak entities use a dashed-underlined attribute called a discriminator. To identify a weak entity, combine the Strong Entity's Primary Key + the Discriminator."
            },
            {
                "type": "list",
                "heading": "2. Attributes: The 'Properties'",
                "content": "Attributes describe the characteristics of an entity.\n\n• **Simple:** Atomic values that cannot be divided (e.g., Age, Gender).\n• **Composite:** Attributes that can be broken down into sub-parts. (e.g., Name $\\rightarrow$ First_Name, Last_Name). *Tip: Always store sub-parts natively in a real DB.*\n• **Multi-valued:** Can have more than one value for a single entity (e.g., Phone Numbers). Visual: **Double Oval**.\n• **Derived:** Not stored physically but calculated (e.g., Age derived from DOB). Visual: **Dashed Oval**."
            },
            {
                "type": "list",
                "heading": "3. Relationships & Cardinality",
                "content": "Relationships represent how entities interact. Cardinality defines numerical constraints.\n\n• **One-to-One (1:1):** One instance of A is related to exactly one instance of B. (e.g., User has one Passport).\n• **One-to-Many (1:N):** One A relates to many B's, but B relates to only one A. (e.g., Department has many Employees).\n• **Many-to-Many (M:N):** Many instances of A relate to many instances of B. (e.g., Students enroll in many Courses). **Crucial Implementation:** M:N relationships must physically be broken into a 'Junction Table' in an RDBMS."
            },
            {
                "type": "list",
                "heading": "4. Participation Constraints",
                "content": "Defines whether the existence of an entity depends on its being related to another entity.\n\n• **Total Participation (Mandatory):** Every entity must be involved in the relationship. (e.g., Every Loan MUST be tied to a Customer). Visual: **Double Line**.\n• **Partial Participation (Optional):** Entities can exist without being part of the relationship. (e.g., Not every employee has to manage a department). Visual: **Single Line**."
            },
            {
                "type": "text",
                "heading": "SQL Example",
                "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- ER Diagram to Tables Conversion\n-- Entity: Student\nCREATE TABLE Student (student_id INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100));\n\n-- Entity: Course\nCREATE TABLE Course (course_id INT PRIMARY KEY, title VARCHAR(100), credits INT);\n\n-- Relationship: Enrolls (M:N creates junction table)\nCREATE TABLE Enrolls (\n    student_id INT, course_id INT, enrollment_date DATE, grade CHAR(2),\n    PRIMARY KEY (student_id, course_id),\n    FOREIGN KEY (student_id) REFERENCES Student(student_id),\n    FOREIGN KEY (course_id) REFERENCES Course(course_id)\n);\n\n-- Weak Entity: Dependent (depends on Employee)\nCREATE TABLE Dependent (\n    emp_id INT, dependent_name VARCHAR(100),\n    PRIMARY KEY (emp_id, dependent_name),\n    FOREIGN KEY (emp_id) REFERENCES Employee(emp_id)\n);</pre>"
            }
        ]
    }

    normalization_topic = {
        "id": "normalization",
        "title": "Normalization",
        "description": "Organizing data in a database to reduce data redundancy (duplication) and improve data integrity.",
        "cards": [
            {
                "type": "text",
                "heading": "Introduction: Eliminating Anomalies",
                "content": "Normalization involves breaking down large, complex tables into smaller, related tables and defining relationships between them.\n\nThe primary goal is to avoid **Anomalies**:\n• **Insertion Anomaly:** Being unable to add data because some other data is missing.\n• **Update Anomaly:** Updating data in one place but not another, leading to inconsistency.\n• **Deletion Anomaly:** Accidental loss of data when deleting a related record."
            },
            {
                "type": "text",
                "heading": "1. First Normal Form (1NF)",
                "content": "A table is in 1NF if it meets the following criteria:\n• Each table cell contains only atomic (indivisible) values.\n• There are no repeating groups or arrays.\n• Each record must be unique (usually identified by a Primary Key).\n\n**Example Violation:** A Student table where the Courses column contains 'Math, Physics, Chemistry.'\n**Solution:** Split the courses into separate rows so each cell has only one value."
            },
            {
                "type": "text",
                "heading": "2. Second Normal Form (2NF)",
                "content": "A table is in 2NF if:\n• It is already in 1NF.\n• It has **No Partial Dependency**. Every non-prime attribute (columns that aren't part of the key) must be fully dependent on the entire Primary Key. (Only applies to composite keys).\n\n**Example Violation:** In an Assignment table with `{Emp_ID, Proj_ID}`, if you have `Emp_Name`, it only depends on `Emp_ID`, not the `Proj_ID`.\n**Solution:** Move `Emp_Name` to a separate Employee table."
            },
            {
                "type": "text",
                "heading": "3. Third Normal Form (3NF)",
                "content": "A table is in 3NF if:\n• It is already in 2NF.\n• It has **No Transitive Dependency**. Non-prime attributes should not depend on other non-prime attributes.\n• *Rule of Thumb:* A column should depend on 'The Key, the Whole Key, and Nothing but the Key.'\n\n**Example Violation:** Employee Table has `Zip_Code` and `City`. City depends on Zip, but Zip is not the PK. `Emp_ID $\\rightarrow$ Zip` and `Zip $\\rightarrow$ City`.\n**Solution:** Create a separate `Zip_Codes` table mapping codes to cities."
            },
            {
                "type": "text",
                "heading": "4. Boyce-Codd (BCNF) & Higher Forms",
                "content": "**BCNF (3.5 NF):**\nA stronger version of 3NF. For every functional dependency $A \\rightarrow B$, $A$ must be a Super Key. It handles cases where a table has overlapping candidate keys.\n\n**Higher Normal Forms:**\n• **4NF:** Deals with Multi-valued Dependencies. (Independent multi-valued facts must not share a table).\n• **5NF:** Project-Join Normal Form (PJNF). Information that can be reconstructed but can't be broken down into strictly two tables without losing data."
            },
            {
                "type": "table",
                "heading": "Comparison Summary for Placements",
                "content": "",
                "headers": ["Normal Form", "Main Requirement", "Eliminates..."],
                "rows": [
                    ["1NF", "Atomic Values", "Repeating groups / arrays"],
                    ["2NF", "Full Functional Dependency", "Partial Dependencies"],
                    ["3NF", "No Transitive Dependency", "Transitive Dependencies"],
                    ["BCNF", "A → B, A must be a Key", "Anomalies from overlapping candidate keys"]
                ]
            },
            {
                "type": "text",
                "heading": "SQL Example",
                "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- UNNORMALIZED (violates 1NF):\n-- Student | Courses\n-- John    | Math, Science, English  ← Multiple values!\n\n-- 1NF: Atomic values\nCREATE TABLE StudentCourses (student_id INT, student_name VARCHAR(100), course VARCHAR(50), instructor VARCHAR(100), instructor_dept VARCHAR(50));\n\n-- 2NF: Remove partial dependencies\nCREATE TABLE Students (student_id INT PRIMARY KEY, name VARCHAR(100));\nCREATE TABLE Courses (course_id INT PRIMARY KEY, course_name VARCHAR(50), instructor VARCHAR(100), instructor_dept VARCHAR(50));\nCREATE TABLE Enrollments (student_id INT, course_id INT, PRIMARY KEY (student_id, course_id));\n\n-- 3NF: Remove transitive dependencies\nCREATE TABLE Instructors (instructor_id INT PRIMARY KEY, name VARCHAR(100), dept VARCHAR(50));\nCREATE TABLE Courses_3NF (course_id INT PRIMARY KEY, course_name VARCHAR(50), instructor_id INT);</pre>"
            }
        ]
    }

    # Replace the topics
    for i, topic in enumerate(data["dbms"]["topics"]):
        if topic["id"] == "er-diagrams":
            data["dbms"]["topics"][i] = er_diagram_topic
        elif topic["id"] == "normalization":
            data["dbms"]["topics"][i] = normalization_topic

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Updated ER Diagrams and Normalization Topics accurately!")
except Exception as e:
    print(f"Error: {e}")
