from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.chat.router import router as chat_router
from app.mcp.client import mcp_client

load_dotenv()

app = FastAPI(name="LangGraph Service")

app.include_router(chat_router, prefix="/api")


@app.on_event("startup")
async def startup_event():
    await mcp_client.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await mcp_client.disconnect()

@app.get("/profile")
async def get_profile():
    result = await mcp_client.call_tool("get_profile", {})
    return result