from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict, Any
import io

from backend.services.chatbot_service import ask_chatbot, export_chat_to_docx

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    history: List[Dict[str, Any]] = []
    api_key: str = ""

@router.post("/chat")
def chat_with_bot(req: ChatRequest):
    response_text = ask_chatbot(req.query, req.history, req.api_key)
    return {"response": response_text}

@router.post("/export")
def export_chat(history: List[Dict[str, Any]] = Body(...)):
    if not history:
        raise HTTPException(status_code=400, detail="History cannot be empty")
        
    doc_bytes = export_chat_to_docx(history)
    return StreamingResponse(
        io.BytesIO(doc_bytes),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": "attachment; filename=chat_export.docx"}
    )
