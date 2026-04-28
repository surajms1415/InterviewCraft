import os
import json
from google import genai
from typing import List, Dict

GENAI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")

import time

def _call_gemini_api(prompt: str) -> str:
    key = GENAI_API_KEY
    if not key or key == "YOUR_GEMINI_API_KEY_HERE":
        raise ValueError("No Gemini API Key provided.")
        
    client = genai.Client(api_key=key)
    models_to_try = ['gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    
    last_error = None
    for model_name in models_to_try:
        max_retries = 2
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                return response.text
            except Exception as e:
                err_str = str(e).lower()
                last_error = e
                if ("503" in err_str or "high demand" in err_str or "unavailable" in err_str):
                    if attempt < max_retries - 1:
                        time.sleep(1)
                        continue
                    else:
                        break # Try next lower model
                elif ("404" in err_str or "not found" in err_str):
                    break # Model not supported, try next lower model immediately
                else:
                    raise e
                    
    raise Exception(f"All fallback models failed. Last error: {str(last_error)}")

def generate_interview_questions(resume_text: str, role: str) -> List[Dict]:
    prompt = f"""
    You are an expert technical interviewer. I will provide you with a candidate's resume text and the role they are applying for.
    Generate a list of 5 personalized interview questions based on their resume. Returns ONLY a JSON array of objects.
    Each object should have:
    - "question": The interview question.
    - "category": "HR", "Technical", or "Project".
    - "suggested_hint": A short hint on how to answer.

    Role: {role}
    Resume Text: {resume_text}
    """
    
    try:
        text_resp = _call_gemini_api(prompt)
        text_resp = text_resp.replace('```json', '').replace('```', '').strip()
        questions = json.loads(text_resp)
        return questions
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return [
            {"question": "Tell me about yourself.", "category": "HR", "suggested_hint": "Focus on your background."},
            {"question": "What is your biggest strength?", "category": "HR", "suggested_hint": "Provide a real example."}
        ]

def evaluate_answer(question: str, applicant_answer: str) -> Dict:
    prompt = f"""
    You are an expert technical interviewer. Evaluate the candidate's answer to the following question.
    Question: {question}
    Answer: {applicant_answer}
    
    Provide your evaluation strictly as a JSON object with:
    - "score": integer from 1 to 10
    - "feedback": Short constructive feedback
    """
    try:
        text_resp = _call_gemini_api(prompt)
        text_resp = text_resp.replace('```json', '').replace('```', '').strip()
        evaluation = json.loads(text_resp)
        return evaluation
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return {"score": 5, "feedback": "Could not evaluate automatically."}
