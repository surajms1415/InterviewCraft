import pdfplumber
import io

def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting PDF: {e}")
    return text

def parse_resume_text(text: str) -> dict:
    # A simple mock NLP extraction for now, pending AI service integration
    # The actual deep extraction will be done via Gemini in ai_generation_service
    skills_keywords = ["Python", "Java", "C++", "React", "FastAPI", "SQL", "Machine Learning", "Docker", "AWS"]
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    
    return {
        "text": text,
        "skills": found_skills,
        "raw_length": len(text)
    }
