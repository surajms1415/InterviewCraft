from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.models import User, InterviewSession, InterviewRound, ResumeData
from backend.schemas.schemas import MockInterviewStart, AnswerSubmission, MockInterviewSessionResponse, AnswerEvaluationResponse
from backend.utils.prompts import generate_interview_question, evaluate_answer
import json

router = APIRouter()

@router.post("/start", response_model=MockInterviewSessionResponse)
def start_interview(data: MockInterviewStart, db: Session = Depends(get_db)):
    # Mocking user auth for now (using user 1)
    user = db.query(User).first()
    if not user:
        user = User(name="Test User", email="test@example.com")
        db.add(user)
        db.commit()
    
    resume = db.query(ResumeData).filter(ResumeData.user_id == user.id).first()
    skills = resume.skills if resume else ["General CS Concepts"]
    
    # Create new session
    session = InterviewSession(user_id=user.id, role=data.role, type=data.type)
    db.add(session)
    db.commit()
    db.refresh(session)
    
    topic = "Data Structures" if data.type == "Technical" else "Behavioral"
    
    first_question = generate_interview_question(
        role=data.role, 
        topic=topic, 
        skills=skills
    )
    
    return {
        "session_id": session.id,
        "message": "Interview started successfully.",
        "first_question": first_question
    }

@router.post("/answer", response_model=AnswerEvaluationResponse)
def submit_answer(data: AnswerSubmission, db: Session = Depends(get_db)):
    session = db.query(InterviewSession).filter(InterviewSession.id == data.session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
        
    evaluation = evaluate_answer(data.question, data.user_answer)
    
    # Save the round
    round_entry = InterviewRound(
        session_id=session.id,
        question=data.question,
        user_answer=data.user_answer,
        ai_evaluation_json=evaluation,
        round_number=data.round_number
    )
    db.add(round_entry)
    db.commit()
    
    # Decide if interview continues (mock limit to 3 rounds)
    is_completed = data.round_number >= 3
    next_question = None
    
    if not is_completed:
        user = db.query(User).filter(User.id == session.user_id).first()
        resume = db.query(ResumeData).filter(ResumeData.user_id == user.id).first()
        skills = resume.skills if resume else ["General"]
        
        # Pull past questions
        past_rounds = db.query(InterviewRound).filter(InterviewRound.session_id == session.id).all()
        past_q = [r.question for r in past_rounds]
        
        # Generate new question based on followup or general
        if "next_followup_question" in evaluation and "Mock" not in evaluation['next_followup_question']:
             next_question = {
                 "question": evaluation['next_followup_question'],
                 "expected_key_points": ["As per follow up structure"],
                 "difficulty": "harder"
             }
        else:
             next_question = generate_interview_question(role=session.role, topic="System Design", skills=skills, previous_questions=past_q)
    else:
        session.is_completed = True
        session.overall_score = evaluation.get("score", 0) # Mock metric
        db.commit()

    return {
        "evaluation": evaluation,
        "next_question": next_question,
        "is_completed": is_completed
    }
