import json

file_path = "frontend-app/src/data/cs_notes.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sp_triggers_topic = {
        "id": "stored-procedures-triggers",
        "title": "Stored Procedures & Triggers",
        "description": "Stored Procedures are precompiled SQL code stored in the database. Triggers are special procedures that automatically execute.",
        "cards": [
            {
                "type": "text",
                "heading": "1. Stored Procedures",
                "content": "A Stored Procedure is a prepared collection of SQL statements that are precompiled and stored in the database. Think of it as a function in traditional programming.\n\n**Mechanics & How it Works:**\n• **Precompilation:** When created, the DBMS parses, checks for errors, and compiles it into an execution plan saved in cache. Calling it later is much faster than raw SQL.\n• **Parameters:** Can accept `IN` parameters (data passed to it), `OUT` parameters (data returned), and `INOUT`.\n• **Execution:** Explicitly called using `CALL` or `EXEC`."
            },
            {
                "type": "text",
                "heading": "Advantages of Stored Procedures for Placements",
                "content": "• **Reduced Network Traffic:** Instead of sending 20 lines of SQL over the network, the app sends one line: `CALL ProcessOrder(101)`.\n• **Security:** Users can be granted permission to execute the procedure without having direct access to underlying tables, preventing unauthorized modifications.\n• **Logic Centralization:** If business logic changes (e.g., tax calculation changes from 5% to 8%), you update the code in one place (the database) rather than in every app."
            },
            {
                "type": "text",
                "heading": "2. Triggers",
                "content": "A Trigger is a special type of stored procedure that automatically executes (or 'fires') in response to a specific event on a particular table or view.\n\n**Mechanics & How it Works:**\n• **Event-Driven:** You cannot manually 'call' a trigger. Triggered by DML events: `INSERT`, `UPDATE`, or `DELETE`.\n• **Timing:**\n  - **BEFORE Trigger:** Fires before data is saved. Used for validation (e.g., Check age > 18).\n  - **AFTER Trigger:** Fires after data is saved. Used for logging or cascading changes.\n• **Special Tables:** Triggers use virtual tables `INSERTED` (or `NEW`) and `DELETED` (or `OLD`) to access changing data."
            },
            {
                "type": "text",
                "heading": "Trigger Use Cases",
                "content": "• **Auditing:** Recording who changed a record and when into an audit table.\n• **Data Integrity:** Ensuring that if a row is deleted from the Users table, all related rows in Orders are handled (referential integrity).\n• **Derived Columns:** Automatically updating a `Total_Sales` column in a Department table whenever a new Sale is inserted."
            },
            {
                "type": "table",
                "heading": "3. Comparison Summary",
                "content": "",
                "headers": ["Feature", "Stored Procedure", "Trigger"],
                "rows": [
                    ["Execution", "Manually called by a user/app.", "Automatically fired by an event."],
                    ["Input/Output", "Can accept and return parameters.", "Cannot accept or return parameters."],
                    ["Transaction", "Can commit or rollback internally.", "Cannot commit/rollback; part of the main transaction."],
                    ["Usage", "General logic, batch processing.", "Auditing, complex integrity checks."]
                ]
            },
            {
                "type": "text",
                "heading": "SQL Example",
                "content": "<pre class='bg-gray-100 p-4 rounded-lg overflow-x-auto text-sm text-gray-800 font-mono'>-- Stored Procedure\nDELIMITER //\nCREATE PROCEDURE TransferMoney(IN from_acc INT, IN to_acc INT, IN amount DECIMAL(10,2))\nBEGIN\n    DECLARE bal DECIMAL(10,2);\n    SELECT balance INTO bal FROM Accounts WHERE account_id = from_acc;\n    IF bal >= amount THEN\n        START TRANSACTION;\n        UPDATE Accounts SET balance = balance - amount WHERE account_id = from_acc;\n        UPDATE Accounts SET balance = balance + amount WHERE account_id = to_acc;\n        COMMIT;\n    END IF;\nEND //\nDELIMITER ;\n\n-- Trigger for Audit Log\nCREATE TRIGGER salary_audit\nAFTER UPDATE ON Employees FOR EACH ROW\nBEGIN\n    IF OLD.salary != NEW.salary THEN\n        INSERT INTO EmployeeAudit (emp_id, old_salary, new_salary, changed_at)\n        VALUES (NEW.emp_id, OLD.salary, NEW.salary, NOW());\n    END IF;\nEND;</pre>"
            }
        ]
    }

    for i, topic in enumerate(data["dbms"]["topics"]):
        if topic["id"] == "stored-procedures-triggers":
            data["dbms"]["topics"][i] = sp_triggers_topic

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Updated Stored Procedures & Triggers Topic accurately!")
except Exception as e:
    print(f"Error: {e}")
