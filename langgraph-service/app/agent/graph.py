from langgraph.graph import StateGraph, END
from typing import TypedDict, Any

from app.agent.nodes import (
    intent_node,
    param_resolver_node,
    tool_executor_node,
    response_node,
)


class AgentState(TypedDict, total=False):
    user_input: str
    tool_name: str
    tool_params: dict
    tool_result: Any
    final_answer: str


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("intent", intent_node)
    graph.add_node("param_resolver", param_resolver_node)
    graph.add_node("tool_executor", tool_executor_node)
    graph.add_node("response", response_node)

    graph.set_entry_point("intent")

    graph.add_edge("intent", "param_resolver")
    graph.add_edge("param_resolver", "tool_executor")
    graph.add_edge("tool_executor", "response")
    graph.add_edge("response", END)

    return graph.compile()


agent = build_graph()