import json

filepath = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\cs_topics.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for category in data['dbms']['categories']:
    if "Keys in DBMS" in category['name']:
        category['topics'] = [
            {"name": "Super Key", "explanation": "A set of one or more columns (attributes) that can uniquely identify a row in a table. It is the most general type of key and may contain redundant attributes."},
            {"name": "Candidate Key", "explanation": "A minimal Super Key. It contains the exact minimum number of attributes necessary to uniquely identify a row. There are no redundant attributes. A table can have multiple Candidate Keys."},
            {"name": "Primary Key", "explanation": "The main Candidate Key selected by the database designer to uniquely identify records. It cannot contain NULL values and must be strictly unique."},
            {"name": "Foreign Key", "explanation": "A column or set of columns that references the Primary Key of another table. It establishes a link (relationship) between the data in two tables, ensuring referential integrity."},
            {"name": "Alternate Key", "explanation": "Any Candidate Key that was NOT selected to be the Primary Key. They still possess unique identification properties but act as secondary keys."},
            {"name": "Composite Key", "explanation": "A Primary Key that consists of two or more columns acting together to uniquely identify a row. Individually, the columns may not be unique."}
        ]
    elif "Normalization" in category['name']:
        category['topics'] = [
            {
                "name": "1NF (First Normal Form)", 
                "explanation": "Rule 1: Each cell must contain a single (atomic) value. Rule 2: Each record needs to be unique. Cannot contain repeating groups or arrays of data.",
                "example": "Instead of [John | Java, C++] in one cell, use two separate rows: [John | Java] and [John | C++]."
            },
            {
                "name": "2NF (Second Normal Form)", 
                "explanation": "Rule 1: Must already be in 1NF. Rule 2: Ensure no partial dependencies. All non-key attributes must depend on the ENTIRE Primary Key, not just a part of a composite key."
            },
            {
                "name": "3NF (Third Normal Form)", 
                "explanation": "Rule 1: Must already be in 2NF. Rule 2: Ensure no transitive dependencies. A non-key attribute cannot depend on another non-key attribute. Everything must depend ONLY on the primary key."
            },
            {
                "name": "BCNF (Boyce-Codd Normal Form)", 
                "explanation": "A stricter, stronger version of 3NF. Rule: For every non-trivial functional dependency X -> Y, X must be a Super Key."
            }
        ]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
print("Updated Cards successfully")
