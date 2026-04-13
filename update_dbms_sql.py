import json

filepath = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\cs_topics.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

dbms_categories = data['dbms']['categories']

new_category = {
    "name": "8. SQL Step-by-Step Deep Dive",
    "topics": [
        {
            "name": "1. Basic SQL (SELECT, UPDATE, DELETE)",
            "explanation": "Understand how the DBMS processes queries internally.",
            "example": "SELECT * FROM Students WHERE age > 20;\n\nExecution:\n1. FROM: DBMS loads Students table.\n2. WHERE: Scans row by row.\nRow 1 -> age=21 -> TRUE\nRow 2 -> age=19 -> FALSE\nRow 3 -> age=22 -> TRUE\n3. SELECT: Returns filtered rows.\n\nUPDATE Execution: Locates row -> modifies in-place -> writes transaction log.\nDELETE Execution: Scans -> checks condition -> marks as deleted."
        },
        {
            "name": "2. JOINS Deep Understanding",
            "explanation": "Joins execute like nested loops internally. Only matching pairs survive in INNER JOIN.",
            "example": "INNER JOIN Execution:\nTake first row from Left Table. Compare with Right Table. If match -> output row. Next row, repeat.\n\nLEFT JOIN Execution:\nStart with Left Table. Match found -> append row. No match -> fill NULL.\nKey Idea: Left table connects to right, preserved at all costs."
        },
        {
            "name": "3. GROUP BY + Aggregation",
            "explanation": "GROUP BY reduces rows by creating buckets. HAVING filters these aggregate buckets.",
            "example": "SELECT dept, COUNT(*) FROM Emp GROUP BY dept HAVING COUNT(*) > 1;\n\nExecution:\n1. FROM: Load Emp.\n2. GROUP BY: Create groups (IT -> [5000, 6000], HR -> [4000]).\n3. Aggregation (COUNT): IT -> 2, HR -> 1.\n4. HAVING: IT(2)>1 -> Keep, HR(1)>1 -> Remove."
        },
        {
            "name": "4. Subquery Execution Flow",
            "explanation": "Inner queries run before outer queries contextually filter results.",
            "example": "SELECT name FROM Students WHERE id IN (SELECT student_id FROM Marks);\n\nExecution:\nStep 1: Inner runs first -> returns list [1, 3].\nStep 2: Outer checks each row. If id is in list -> keep, else discard."
        },
        {
            "name": "5. Window Functions vs Group By",
            "explanation": "Window functions process data over groups (windows) without collapsing rows together.",
            "example": "SELECT name, marks, RANK() OVER (ORDER BY marks DESC) FROM Marks;\n\nExecution:\nNo grouping -> rows stay same.\nSort data by marks desc.\nAssign rank based on order.\nKey difference: GROUP BY reduces rows, WINDOW keeps rows."
        }
    ]
}

existing_names = [c['name'] for c in dbms_categories]
if "8. SQL Step-by-Step Deep Dive" in existing_names:
    for i, c in enumerate(dbms_categories):
        if c['name'] == "8. SQL Step-by-Step Deep Dive":
            dbms_categories[i] = new_category
else:
    dbms_categories.append(new_category)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
print('Updated DBMS SQL Deep Dive')
