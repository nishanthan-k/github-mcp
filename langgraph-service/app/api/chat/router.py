from fastapi import APIRouter
from app.api.chat.models import ChatRequest

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/")
async def chat(request: ChatRequest):
    return {"message": "Hello, World!"}
