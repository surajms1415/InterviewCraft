import os
import json
from google import genai

GENAI_API_KEY = os.getenv("GENAI_API_KEY", "")

import time

def _call_gemini_api(prompt: str, api_key: str = "") -> str:
    key = api_key.strip() if api_key and api_key.strip() else GENAI_API_KEY
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
                        time.sleep(1) # Quick wait before retrying same model
                        continue
                    else:
                        break # Exhausted retries for this model, try next lower model
                elif ("404" in err_str or "not found" in err_str):
                    break # Model doesn't exist for this key, try next lower model immediately
                else:
                    raise e # Critical error like invalid key, do not fallback
                    
    raise Exception(f"All fallback models failed. Last error: {str(last_error)}")

def generate_interview_question(role: str, topic: str, skills: list, previous_questions: list = None) -> dict:
    prompt = f"""
    You are an expert technical interviewer for a {role} position.
    The candidate has the following skills: {', '.join(skills)}.
    The topic for this question is: {topic}.
    
    Already asked questions: {previous_questions or []}. Do not repeat these.
    
    Generate a technical interview question for the candidate. Return ONLY valid JSON in this format:
    {{
        "question": "The main question text",
        "expected_key_points": ["point 1", "point 2"],
        "difficulty": "medium"
    }}
    """
    if not GENAI_API_KEY:
        return {
            "question": f"Mock Question: Explain how {topic} works in {role}?",
            "expected_key_points": ["Mock point 1"],
            "difficulty": "medium"
        }
        
    try:
        text = _call_gemini_api(prompt)
        text = text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)
    except Exception as e:
        return {"error": str(e), "question": "Could not generate question."}

def evaluate_answer(question: str, user_answer: str) -> dict:
    prompt = f"""
    You are a strict technical interviewer evaluating an answer.
    Question asked: "{question}"
    Candidate's Answer: "{user_answer}"
    
    Evaluate this answer for technical correctness and communication clarity. Return ONLY valid JSON:
    {{
        "score": 8,
        "technical_correctness": "Brief feedback on technical details.",
        "communication_clarity": "Brief feedback on structure and clarity.",
        "ideal_answer": "What the perfect answer should have been.",
        "next_followup_question": "A logical follow-up question based on the answer."
    }}
    """
    if not GENAI_API_KEY:
        return {
            "score": 7,
            "technical_correctness": "Mock Correctness Feedback",
            "communication_clarity": "Mock Comm Feedback",
            "ideal_answer": "Mock Ideal",
            "next_followup_question": "Mock Followup?"
        }
        
    try:
        text = _call_gemini_api(prompt)
        text = text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)
    except Exception as e:
        return {"error": str(e), "score": 0}

def analyze_resume_text(resume_text: str) -> dict:
    prompt = f"""
    You are an ATS (Applicant Tracking System) and technical recruiter. 
    Analyze the following resume text:
    
    "{resume_text}"
    
    Extract insights and return ONLY valid JSON in this format:
    {{
        "ats_score": 75,
        "detected_skills": ["Skill1", "Skill2"],
        "detected_projects": [{{"title": "ProjectName", "desc": "Short logic"}}],
        "weaknesses": ["Issue1", "Issue2"],
        "improvement_suggestions": ["Suggestion1"],
        "generated_hr_questions": ["HR Q1", "HR Q2"]
    }}
    """
    if not GENAI_API_KEY:
        return {
            "ats_score": 50,
            "detected_skills": ["Python", "Mock"],
            "detected_projects": [],
            "weaknesses": ["No APIKey configured"],
            "improvement_suggestions": [],
            "generated_hr_questions": []
        }
    
    try:
        text = _call_gemini_api(prompt)
        text = text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)
    except Exception as e:
        return {"error": str(e)}

def generate_intense_hr_questions(resume_text: str, github_link: str, github_projects_info: str = "", api_key: str = "") -> list:
    prompt = f"""
    SYSTEM INSTRUCTION:
    You are an elite, FAANG-level Technical Recruiter and Principal Engineer conducting a rigorous final-round interview. Your goal is to drill deep into the candidate's actual experience and expose their architectural limits. Produce extremely intense, highly specific, and challenging behavioral & technical-screening questions.
    
    The candidate has provided the following GitHub link: {github_link}
    Here is an overview of their GitHub projects:
    {github_projects_info}
    
    And the following Resume text (if any): "{resume_text}"
    
    CRITICAL INSTRUCTIONS:
    1. Do NOT ask generic or basic questions. Do NOT ask "What is polymorphism?" or "Explain your project."
    2. Analyze the specific technologies, roles, and complexity found in their Resume and GitHub.
    3. Generate exactly 4-5 intense questions that ask about architectural trade-offs, failures, scaling bottlenecks, severe technical debt, and managing extreme professional conflicts.
    4. Provide a detailed solution or the ideal way to reply for each question. YOU MUST format the solution using Markdown bullet points (- or *) to make it easy to read in a list format. Do not write a solid paragraph.
    
    Return ONLY a valid JSON object with a single "questions" array containing exactly 4-5 objects.
    Each object must have "question" and "solution" string keys.
    Example Format:
    {{
        "questions": [
            {{
                "question": "You used React for your frontend. How exactly did you mitigate prop-drilling in your dashboard, and why didn't you choose Zustand over Redux?",
                "solution": "- **Trade-offs**: Focus on state management trade-offs.\\n- **Architecture**: Discuss component architecture.\\n- **Scaling**: Address scaling complexity and re-renders."
            }}
        ]
    }}
    """
    
    try:
        text = _call_gemini_api(prompt, api_key=api_key)
        text = text.replace('```json', '').replace('```', '').strip()
        data = json.loads(text)
        if isinstance(data, dict) and "questions" in data:
            return data["questions"]
        return data if isinstance(data, list) else []
    except Exception as e:
        return [f"Error generating questions: {str(e)}"]
