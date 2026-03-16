from typing import TypedDict


class AgentState(TypedDict):
    user_input: str
    tool_name: str
    tool_params: dict
    tool_result: dict
    final_answer: str