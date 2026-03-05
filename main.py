from langgraph.graph import StateGraph
from graph import search, build_dependencies, AgentState

if __name__ == "__main__":
    graph = StateGraph(AgentState)
    graph.add_node('search', search)
    graph.set_entry_point('search')
    graph.set_finish_point('search')
    app = graph.compile()
    res = app.invoke({
        'commodity_name': 'copper',
        'search_result': [],
        'dependency_graph': {}
    })
    print(res["search_result"])
