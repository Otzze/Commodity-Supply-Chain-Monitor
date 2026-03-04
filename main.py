from langgraph.graph import StateGraph
from stateGraph import search, build_dependencies, AgentState

if __name__ == "__main__":
    graph = StateGraph(AgentState)
    graph.add_node('search', search)
    graph.add_node('build_dependencies', build_dependencies)
    graph.set_entry_point('search')
    graph.set_finish_point('build_dependencies')
    app = graph.compile()
    res = app.invoke({
        'commodity_name': 'steel',
        'search_result': [],
        'dependency_graph': {}
    })
    print(res)
