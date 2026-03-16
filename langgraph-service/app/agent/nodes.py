import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from app.mcp.client import mcp_client

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)


async def intent_node(state: dict):
    tools = await mcp_client.list_tools()

    prompt = f"""
You select the correct tool for a request.

Available tools:
{tools}

User request:
{state["user_input"]}

Return only the tool name.
"""

    response = await llm.ainvoke([
        SystemMessage(content="Select the most appropriate tool."),
        HumanMessage(content=prompt)
    ])

    return {
        **state,
        "tool_name": response.content.strip()
    }


async def param_resolver_node(state: dict):
    tool_name = state["tool_name"]
    user_input = state["user_input"]

    prompt = f"""
Extract parameters required for the tool.

Tool: {tool_name}

User request:
{user_input}

Return JSON only.
"""

    response = await llm.ainvoke([
        SystemMessage(content="Extract parameters for tool execution."),
        HumanMessage(content=prompt)
    ])

    try:
        params = json.loads(response.content)
    except Exception:
        params = {}

    return {
        **state,
        "tool_params": params
    }


async def tool_executor_node(state: dict):
    tool_name = state["tool_name"]
    params = state.get("tool_params", {})

    result = await mcp_client.call_tool(tool_name, params)

    return {
        **state,
        "tool_result": result
    }


async def response_node(state: dict):
    user_input = state["user_input"]
    tool_result = state["tool_result"]

    prompt = f"""
User request:
{user_input}

Tool output:
{tool_result}

Provide a clear response for the user.
"""

    response = await llm.ainvoke([
        SystemMessage(content="Generate the final answer for the user."),
        HumanMessage(content=prompt)
    ])

    return {
        **state,
        "final_answer": response.content
    }