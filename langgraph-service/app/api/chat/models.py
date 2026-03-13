from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(description="User prompt for the chat")