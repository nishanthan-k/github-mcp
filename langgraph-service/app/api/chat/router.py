from fastapi import APIRouter
from app.api.chat.models import ChatRequest
from app.agent.graph import agent

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/")
async def chat(request: ChatRequest):
    result = await agent.ainvoke({
    "user_input": request.prompt
    })

    return result["final_answer"]
