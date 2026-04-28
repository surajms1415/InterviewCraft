from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.models import User, ResumeData, InterviewSession, PerformanceLog
from backend.schemas.schemas import DashboardStats

router = APIRouter()

@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        return DashboardStats(
            total_interviews=0, avg_score=0.0, ats_score=0, recent_logs=[], recommendation="Upload a resume to start!"
        )
        
    sessions = db.query(InterviewSession).filter(InterviewSession.user_id == user.id, InterviewSession.is_completed == True).all()
    resume = db.query(ResumeData).filter(ResumeData.user_id == user.id).first()
    logs = db.query(PerformanceLog).filter(PerformanceLog.user_id == user.id).order_by(PerformanceLog.timestamp.desc()).limit(5).all()
    
    total_int = len(sessions)
    avg_score = sum([s.overall_score for s in sessions if s.overall_score]) / total_int if total_int > 0 else 0.0
    ats = resume.ats_score if resume else 0
    
    formatted_logs = [{"topic": l.topic, "score": l.score, "date": l.timestamp.strftime("%Y-%m-%d")} for l in logs]
    
    return DashboardStats(
        total_interviews=total_int,
        avg_score=round(avg_score, 1),
        ats_score=ats,
        recent_logs=formatted_logs,
        recommendation="Focus on System Design based on your recent weak scores."
    )
