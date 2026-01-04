from langgraph.graph import StateGraph, END
from state import GraphState
from nodes.code_indexer import code_indexer_node

def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("code_indexer", code_indexer_node)
    graph.set_entry_point("code_indexer")
    graph.add_edge("code_indexer", END)

    return graph.compile()
