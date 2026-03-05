import asyncio
from graph import create_graph, AgentState

async def main():
    app = await create_graph()
    initial_state = {
        'commodity_name': 'copper',
        'messages': [],
        'dependency_graph': {}
    }
    # 3. Invoke the graph asynchronously
    print(f"--- Running analysis for {initial_state['commodity_name']} ---")
    async for event in app.astream(initial_state):
        for node, output in event.items():
            print(f"--- Node: {node} ---")
            if "messages" in output:
                last_msg = output["messages"][-1]
                if last_msg.content:
                    print(f"Content: {last_msg.content}")
                if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
                    print(f"Tool calls: {last_msg.tool_calls}")

if __name__ == "__main__":
    asyncio.run(main())
