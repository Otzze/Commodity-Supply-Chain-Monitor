from typing import List, TypedDict, Dict

class AgentState(TypedDict):
    commodity_name: str
    search_result: List[str]
    dependency_graph: Dict

def search(state: AgentState) -> AgentState:
    """ Search Agent Node for supply lines of the commodity"""
    return state

def build_dependencies(state: AgentState) -> AgentState:
    """ Dependency Builder Node for building the dependency graph"""
    return state
