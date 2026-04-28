import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import engine, Base
from backend.routes import interview, resume, dashboard, learning, chatbot

# Create Database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="PrepForge AI API", description="Production API for PrepForge AI placement platform")

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(resume.router, prefix="/api/resume", tags=["Resume"])
app.include_router(interview.router, prefix="/api/interview", tags=["Interview"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(learning.router, prefix="/api/learning", tags=["Learning"])
app.include_router(chatbot.router, prefix="/api", tags=["Chatbot"])

@app.get("/")
def read_root():
    return {"message": "Welcome to PrepForge AI API"}
