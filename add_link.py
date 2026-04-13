import os

link_text = """    <p style="font-size: 0.9rem; margin-bottom: 0.5rem;">To power real-time AI capabilities, enter your Gemini API Key below. This key is securely saved locally in your browser.</p>
    <p style="font-size: 0.85rem; margin-bottom: 1rem; color: var(--secondary-color);">Don't have one? <a href="https://aistudio.google.com/app/apikey" target="_blank" style="color: var(--primary-color); text-decoration: underline;">Get your free Gemini API Key here</a> (Takes 1 minute). Just login, click "Create API key", and paste it below!</p>"""

for file_name in ['hr_interview.html', 'chatbot.html']:
    filepath = rf'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\templates\{file_name}'
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    old_p = '<p style="font-size: 0.9rem; margin-bottom: 1rem;">To power real-time AI capabilities, enter your Gemini API Key below. This key is saved locally in your browser.</p>'
    html = html.replace(old_p, link_text)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated links!")
