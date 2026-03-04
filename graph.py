from typing import List, TypedDict, Dict
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    commodity_name: str
    search_result: List[BaseMessage]
    dependency_graph: Dict

def search(state: AgentState) -> AgentState:
    """ Search Agent Node for supply lines of the commodity"""
    return state

def impact_agent(state: AgentState) -> AgentState:
    """ Impact Agent Node for analyzing the impact of supply line disruptions"""
    return state

def build_dependencies(state: AgentState) -> AgentState:
    """ Dependency Builder Node for building the dependency graph"""
    return state
