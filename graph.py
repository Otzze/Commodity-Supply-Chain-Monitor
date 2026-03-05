import os
import asyncio
from typing import List, TypedDict, Dict, Annotated, Union
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage, ToolMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from tools import init_tools

class AgentState(TypedDict):
    commodity_name: str
    messages: Annotated[List[BaseMessage], lambda x, y: x + y]
    dependency_graph: Dict

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    max_tokens=None,
)

async def search_agent(state: AgentState):
    """ Search Agent Node that decides whether to search """
    tools = await init_tools()
    llm_with_tools = llm.bind_tools(tools)

    system_prompt = (
        "You are a supply line analyst. Your task is to provide fresh information "
        f"and news about the supply lines of {state['commodity_name']}. "
        "Use the 'brave_news_search' tool to find recent updates and news. "
    )

    messages = [SystemMessage(content=system_prompt)] + state.get("messages", [])
    if not any(isinstance(m, HumanMessage) for m in messages):
        messages.append(HumanMessage(content=f"What is the current news and supply chain status for {state['commodity_name']}?"))

    res = await llm_with_tools.ainvoke(messages)
    return {"messages": [res]}

def should_continue(state: AgentState):
    """ Decide whether to call tools or end """
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return END

async def create_graph():
    """ Initialize tools and compile the graph """
    tools = await init_tools()
    tool_node = ToolNode(tools)

    workflow = StateGraph(AgentState)

    workflow.add_node("agent", search_agent)
    workflow.add_node("tools", tool_node)

    workflow.set_entry_point("agent")

    workflow.add_conditional_edges(
        "agent",
        should_continue,
    )

    workflow.add_edge("tools", "agent")

    return workflow.compile()
