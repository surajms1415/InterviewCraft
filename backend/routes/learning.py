from fastapi import APIRouter
from typing import List

router = APIRouter()

# Note: In a fully productionized setup, this could read from a db table.
# For now we supply via API to allow easy migration to DB updates later.
cs_topics = [
    {
        "id": "os", 
        "title": "Operating Systems", 
        "description": "Dive deep into Operating Systems. OS Fundamentals, Process Management, Memory Management, and Interview Questions.",
        "pdfLink": "https://www.wcode.in/notes/OS.pdf"
    },
    {
        "id": "dbms", 
        "title": "DBMS", 
        "description": "Master Database Management Systems and SQL. Database fundamentals, ACID properties, normalization, keys, ER diagrams, relational algebra.",
        "pdfLink": "https://www.wcode.in/notes/DBMS.pdf"
    },
    {
        "id": "cn", 
        "title": "Computer Networks", 
        "description": "Complete CN notes with OSI, TCP/IP, protocols. Learn network layers, routing protocols, and prepare for CN interviews.",
        "pdfLink": "https://www.wcode.in/notes/CN.pdf"
    },
    {
        "id": "oop", 
        "title": "Object Oriented Programming", 
        "description": "Master OOPs with inheritance, polymorphism, design patterns, encapsulation, and abstractions.",
        "pdfLink": "https://www.wcode.in/notes/OOPS.pdf"
    }
]

gd_topics = [
    {"id": 1, "topic": "AI in the Workplace: Boon or Bane?", "point": "Increases efficiency", "reason": "Automates repetitive tasks", "example": "Chatbots in customer service"},
    {"id": 2, "topic": "Remote Work vs Office", "point": "Better work-life balance", "reason": "No commute time", "example": "Working from home post-COVID"}
]

@router.get("/cs-subjects", response_model=List[dict])
def get_cs_subjects():
    return cs_topics

@router.get("/gd-topics", response_model=List[dict])
def get_gd_topics():
    return gd_topics
