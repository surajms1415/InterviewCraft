from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    resume_data = relationship("ResumeData", back_populates="user", uselist=False)
    interview_sessions = relationship("InterviewSession", back_populates="user")
    performance_logs = relationship("PerformanceLog", back_populates="user")
    daily_tasks = relationship("DailyTask", back_populates="user")

class ResumeData(Base):
    __tablename__ = "resume_data"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    skills = Column(JSON, default=list)
    projects = Column(JSON, default=list)
    ats_score = Column(Integer)
    analysis_json = Column(JSON)
    
    user = relationship("User", back_populates="resume_data")

class InterviewSession(Base):
    __tablename__ = "interview_sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role = Column(String)  # SDE / Analyst / Core / HR
    type = Column(String)  # HR / Technical / Mixed
    overall_score = Column(Integer, nullable=True)
    feedback_json = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_completed = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="interview_sessions")
    rounds = relationship("InterviewRound", back_populates="session", cascade="all, delete")

class InterviewRound(Base):
    __tablename__ = "interview_rounds"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id"))
    question = Column(String)
    user_answer = Column(Text, nullable=True)
    ai_evaluation_json = Column(JSON, nullable=True)
    round_number = Column(Integer)
    
    session = relationship("InterviewSession", back_populates="rounds")

class PerformanceLog(Base):
    __tablename__ = "performance_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic = Column(String)
    score = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="performance_logs")

class DailyTask(Base):
    __tablename__ = "daily_tasks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_desc = Column(String)
    is_completed = Column(Boolean, default=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="daily_tasks")
