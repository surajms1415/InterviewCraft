from pydantic import BaseModel
from typing import List, Optional, Any

class ResumeUploadResponse(BaseModel):
    message: str
    resume_id: int
    ats_score: int
    analysis: Any

class MockInterviewStart(BaseModel):
    role: str
    type: str

class MockInterviewSessionResponse(BaseModel):
    session_id: int
    message: str
    first_question: dict

class AnswerSubmission(BaseModel):
    session_id: int
    question: str
    user_answer: str
    round_number: int

class AnswerEvaluationResponse(BaseModel):
    evaluation: dict
    next_question: Optional[dict]
    is_completed: bool

class DashboardStats(BaseModel):
    total_interviews: int
    avg_score: float
    ats_score: int
    recent_logs: List[dict]
    recommendation: str

class DailyTaskBase(BaseModel):
    id: int
    task_desc: str
    is_completed: bool

class DailyMissionResponse(BaseModel):
    tasks: List[DailyTaskBase]
