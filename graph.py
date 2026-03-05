from typing import List, TypedDict, Dict
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage

class AgentState(TypedDict):
    commodity_name: str
    search_result: List[AIMessage]
    dependency_graph: Dict

llm = ChatGroq(
    model="qwen/qwen3-32b",
    max_tokens=None,
)

def search(state: AgentState) -> AgentState:
    """ Search Agent Node for supply lines of the commodity"""
    message = [
            (
                "system",
                f"You are a supply line analyst. Your task is to search for the supply lines of {state['commodity_name']} and provide relevant information.",
            )
    ]

    res = llm.invoke(message)
    state["search_result"].append(res)
    return state

def impact_agent(state: AgentState) -> AgentState:
    """ Impact Agent Node for analyzing the impact of supply line disruptions"""
    return state

def build_dependencies(state: AgentState) -> AgentState:
    """ Dependency Builder Node for building the dependency graph"""
    return state
