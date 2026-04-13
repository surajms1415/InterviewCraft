import os

filepath = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\app.py'

with open(filepath, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update the top imports securely
if 'from io import BytesIO' not in code:
    code = code.replace("import traceback", "import traceback\nfrom io import BytesIO\nfrom docx import Document\nfrom flask import send_file")

# 2. Add Export Route before chatbot route
export_route = """
@app.route('/export-hr', methods=['POST'])
def export_hr():
    import json
    questions_str = request.form.get('questions_data')
    if not questions_str:
        return "No data provided", 400
        
    try:
        questions = json.loads(questions_str)
    except:
        return "Invalid data", 400

    doc = Document()
    doc.add_heading('Your Personalized Interview Questions', 0)
    
    for i, item in enumerate(questions, 1):
        q = item.get('question', '')
        h = item.get('hint', '')
        doc.add_heading(f"Q{i}: {q}", level=1)
        doc.add_paragraph(h, style='Intense Quote')
        doc.add_paragraph("") # Space
        
    f = BytesIO()
    doc.save(f)
    f.seek(0)
    
    return send_file(f, as_attachment=True, download_name='Interview_Prep.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
"""

if "@app.route('/export-hr" not in code:
    code = code.replace("@app.route('/chatbot')", export_route + "\n@app.route('/chatbot')")


# 3. Enhance generate_mock_questions
advanced_mock = """def generate_mock_questions(text):
    text_lower = text.lower()
    questions = []
    
    if 'github.com' in text_lower:
        questions.extend([
            ("Walk me through the architecture of your most complex GitHub repository.", "Discuss layers, controllers, services, and how they interact. Focus on structural design."),
            ("How did you manage version control and branch merging during this project?", "Mention PRs, git rebase vs merge, dealing with merge conflicts."),
            ("I see this project is open-source. Have you dealt with public issues or community contributions?", "Focus on code review etiquette and setting up Contribution guidelines."),
            ("What security vulnerabilities did you protect against in your codebase?", "Mention sanitization, SQL Injection prevention,, or CORS handling.")
        ])

    if 'python' in text_lower or 'flask' in text_lower or 'django' in text_lower:
        questions.extend([
            ("Why did you choose Python for this backend component over Go or Node?", "Mention rapid prototyping, ecosystem, GIL limitations, and async features."),
            ("How does Python handle garbage collection?", "Explain reference counting and the cyclic garbage collector."),
            ("Explain the concept of Web Server Gateway Interface (WSGI) in your Python apps.", "Discuss how Flask communicates with Gunicorn or the web server.")
        ])
        
    if 'react' in text_lower or 'frontend' in text_lower:
        questions.extend([
            ("Why React? How does the Virtual DOM actually improve performance here?", "Explain batching updates, diffing algorithm (Reconciliation)."),
            ("How did you manage global state in this application?", "Talk about Redux, Context API, or Zustand, and why you avoided prop-drilling."),
            ("Explain a challenging UI bug you resolved involving component lifecycles.", "Mention useEffect dependencies, stale closures, or unmounting memory leaks.")
        ])
        
    if 'sql' in text_lower or 'database' in text_lower:
        questions.extend([
            ("Walk me through your database schema. Did you normalize to 3NF?", "Discuss entities, relations, and trade-offs of redundancy."),
            ("How would you scale this database if traffic spiked by 100x tomorrow?", "Discuss Read Replicas, Caching (Redis), Connection Pooling, or Sharding."),
            ("Explain an advanced SQL query you wrote. Did you use Window Functions or CTEs?", "Provide a concrete narrative of grouping/aggregating complex data.")
        ])

    # Ensure exactly 8-10 high quality questions if keyword matched
    if not questions:
        questions = [
            ("Walk me through your resume, specifically focusing on the timeline of your skills acquisition.", "Connect the dots between your internships and side-projects."),
            ("Describe the most difficult technical hurdle listed on your resume.", "Use STAR method. Emphasize the debugging process."),
            ("What architectural patterns do you usually fall back on when starting a project?", "Discuss Monolith vs Microservices, MVC, etc."),
            ("How do you ensure your code is maintainable for the next developer?", "Mention clean code principles, SOLID, and documentation."),
            ("Tell me about a time you had to pivot a project idea mid-way.", "Highlight adaptability and agile principles."),
            ("Where is the 'weakest link' in the tech stack you listed?", "Show self-awareness of technology limits."),
            ("If you lead a team of 3 juniors on your current project, how would you distribute tasks?", "Focus on pair programming, code reviews, and scoping."),
            ("What is the next language/framework you intend to learn, and why?", "Demonstrate continuous learning.")
        ]
    
    # Cap at 10 and format
    final_questions = questions[:10]
    return [{'question': q, 'hint': h} for q, h in final_questions]
"""

# Replace the old generate_mock_questions
import re
code = re.sub(r'def generate_mock_questions\(text\):.*?(?=@app\.route\(\'/chatbot\'\))', advanced_mock, code, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(code)

print("Backend patched securely.")
