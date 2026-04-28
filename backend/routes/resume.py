from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from typing import Optional
import urllib.request
import json
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.models import User, ResumeData
from backend.schemas.schemas import ResumeUploadResponse
from backend.utils.prompts import analyze_resume_text, generate_intense_hr_questions
import pdfplumber
import io

router = APIRouter()

@router.post("/analyze", response_model=ResumeUploadResponse)
async def analyze_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        
    user = db.query(User).first()
    if not user:
        user = User(name="Test User", email="test@example.com")
        db.add(user)
        db.commit()
    
    # Extract text
    resume_text = ""
    contents = await file.read()
    with pdfplumber.open(io.BytesIO(contents)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                 resume_text += text + "\n"
                 
    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from PDF.")
        
    analysis = analyze_resume_text(resume_text)
    
    # Save to db
    resume_entry = db.query(ResumeData).filter(ResumeData.user_id == user.id).first()
    if not resume_entry:
        resume_entry = ResumeData(user_id=user.id)
        db.add(resume_entry)
        
    resume_entry.skills = analysis.get('detected_skills', [])
    resume_entry.projects = analysis.get('detected_projects', [])
    resume_entry.ats_score = analysis.get('ats_score', 0)
    resume_entry.analysis_json = analysis
    
    db.commit()
    db.refresh(resume_entry)
        
    return {
        "message": "Resume analyzed successfully",
        "resume_id": resume_entry.id,
        "ats_score": resume_entry.ats_score,
        "analysis": analysis
    }

@router.post("/generate-hr")
async def generate_hr(github_link: Optional[str] = Form(""), api_key: Optional[str] = Form(""), file: Optional[UploadFile] = File(None)):
    resume_text = ""
    
    if file:
        if not file.filename.endswith('.pdf'):
            raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        
        contents = await file.read()
        with pdfplumber.open(io.BytesIO(contents)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                     resume_text += text + "\n"
                     
    if not github_link.strip() and not resume_text.strip():
        raise HTTPException(status_code=400, detail="Must provide at least a GitHub link or a Resume.")
        
    github_projects_info = ""
    if github_link.strip():
        try:
            # Extract username from link (e.g., https://github.com/username)
            username = github_link.strip().rstrip('/').split('/')[-1]
            url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5"
            req = urllib.request.Request(url, headers={'User-Agent': 'PrepForge'})
            with urllib.request.urlopen(req, timeout=5) as response:
                repos = json.loads(response.read().decode())
                projects = []
                for r in repos:
                    if not r.get('fork'):
                        name = r.get('name', '')
                        desc = r.get('description', 'No description')
                        lang = r.get('language', 'Unknown')
                        projects.append(f"- {name} ({lang}): {desc}")
                if projects:
                    github_projects_info = "\n".join(projects)
        except Exception as e:
            print(f"Error fetching GitHub repos: {e}")
            github_projects_info = "Could not fetch detailed project info."

    questions = generate_intense_hr_questions(resume_text, github_link, github_projects_info, api_key)
    
    return {
        "questions": questions
    }
