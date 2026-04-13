import json
import os

cs_topics_path = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\cs_topics.json'
examples_path = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\examples.json'

with open(cs_topics_path, 'r', encoding='utf-8') as f:
    topics_data = json.load(f)

# Extract category 8 from dbms
sql_deep_dive = None
dbms_categories = topics_data['dbms'].get('categories', [])
for i, cat in enumerate(dbms_categories):
    if cat['name'] == "8. SQL Step-by-Step Deep Dive":
        sql_deep_dive = dbms_categories.pop(i)
        break

# Also, create a detailed Normalization example based on user's hint
normalization_example = {
    "name": "Normalization Step-by-Step (1NF to 3NF)",
    "explanation": "Understanding how to decompose a messy table into a normalized relational schema.",
    "example": "Scenario: You have an 'Orders' table containing multiple items per row.\n\n[Unnormalized]\nOrder1 | John | Apple, Banana | New York\n\n[1NF (Atomic Values)]\nOrder1 | John | Apple  | New York\nOrder1 | John | Banana | New York\n\n[2NF (No Partial Dependency)]\nIf Primary Key is (OrderID, Item), then Name and City only depend on OrderID!\nDecompose:\nTable 1: OrderID -> Name, City\nTable 2: OrderID, Item\n\n[3NF (No Transitive Dependency)]\nIf City depends on Name (John -> New York), New York doesn't directly depend on OrderID.\nDecompose Table 1 further:\nTable 1a: OrderID -> Name\nTable 1b: Name -> City"
}

# Construct examples logic
examples_data = {
    "dbms": {
        "title": "Database Management Systems (DBMS)",
        "description": "Deep-dive examples and execution flows for SQL and Schema Design.",
        "categories": [
            {
                "name": "Schema Design Examples",
                "topics": [normalization_example]
            }
        ]
    }
}

if sql_deep_dive:
    examples_data['dbms']['categories'].append({
        "name": "SQL Step-by-Step Execution Logs",
        "topics": sql_deep_dive['topics']
    })

# Initialize OS, OOP, CN as empty for now
examples_data['os'] = {"title": "Operating Systems (OS)", "description": "OS Examples coming soon.", "categories": []}
examples_data['oop'] = {"title": "Object-Oriented Programming (OOP)", "description": "OOP Examples coming soon.", "categories": []}
examples_data['cn'] = {"title": "Computer Networks (CN)", "description": "CN Examples coming soon.", "categories": []}

# Save files
with open(cs_topics_path, 'w', encoding='utf-8') as f:
    json.dump(topics_data, f, indent=4)

with open(examples_path, 'w', encoding='utf-8') as f:
    json.dump(examples_data, f, indent=4)

print("Data refactored successfully")
