import os

# 1. Update HR Interview template
hr_path = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\templates\hr_interview.html'
with open(hr_path, 'r', encoding='utf-8') as f:
    hr_html = f.read()

api_key_block = """
<div class="mb-4" style="background: var(--bg-color); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 0.5rem;">AI Configuration (For Personalized Extraction)</h3>
    <p style="font-size: 0.9rem; margin-bottom: 1rem;">To power real-time AI capabilities, enter your Gemini API Key below. This key is saved locally in your browser.</p>
    <div style="display: flex; gap: 10px;">
        <input type="password" id="geminiApiKey" class="form-control" placeholder="sk-..." style="max-width: 300px;">
        <button type="button" class="btn active" onclick="saveApiKey()">Save API Key</button>
    </div>
    <p id="apiStatus" style="font-size: 0.8rem; color: var(--secondary-color); margin-top: 0.5rem;"></p>
</div>
<script>
function saveApiKey() {
    const key = document.getElementById('geminiApiKey').value;
    if(key) {
        localStorage.setItem('gemini_api_key', key);
        document.getElementById('apiStatus').innerText = "Key saved successfully!";
        document.getElementById('apiStatus').style.color = "#4ade80";
    } else {
        document.getElementById('apiStatus').innerText = "Please enter a valid key.";
        document.getElementById('apiStatus').style.color = "#ef4444";
    }
}
window.addEventListener('DOMContentLoaded', () => {
    if(localStorage.getItem('gemini_api_key')) {
        document.getElementById('geminiApiKey').value = localStorage.getItem('gemini_api_key');
        document.getElementById('apiStatus').innerText = "API Key loaded from LocalStorage.";
    }
});
</script>
"""

if "AI Configuration" not in hr_html:
    hr_html = hr_html.replace('<h2 class="mb-4" style="color: var(--primary-color); text-align: center;">HR Interview Preparation</h2>', 
                              '<h2 class="mb-4" style="color: var(--primary-color); text-align: center;">HR Interview Preparation</h2>\n' + api_key_block)

export_block = """
        <form action="{{ url_for('export_hr') }}" method="POST" style="margin-bottom: 20px;">
            <input type="hidden" name="questions_data" value="{{ generated_questions | tojson | forceescape }}">
            <button type="submit" class="btn active">Export to Word (.docx)</button>
        </form>
"""
if "Export to Word" not in hr_html:
    hr_html = hr_html.replace('<h3 class="mb-2" style="color: var(--primary-color);">Your Personalized Interview Questions:</h3>',
                              '<div style="display: flex; justify-content: space-between; align-items: center;"><h3 class="mb-2" style="color: var(--primary-color);">Your Personalized Interview Questions:</h3>\n' + export_block + "</div>")

with open(hr_path, 'w', encoding='utf-8') as f:
    f.write(hr_html)

# 2. Update Chatbot template
chat_path = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\templates\chatbot.html'
with open(chat_path, 'r', encoding='utf-8') as f:
    chat_html = f.read()

if "AI Configuration" not in chat_html:
    chat_html = chat_html.replace('<h2 class="mb-2" style="color: var(--primary-color);">AI Doubt Solver</h2>',
                                  '<h2 class="mb-2" style="color: var(--primary-color);">AI Doubt Solver</h2>\n' + api_key_block)

with open(chat_path, 'w', encoding='utf-8') as f:
    f.write(chat_html)

print("Updated UI successfully.")
