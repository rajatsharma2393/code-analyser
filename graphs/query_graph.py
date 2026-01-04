from langgraph.graph import StateGraph, END
from state import GraphState
from nodes.classifier import classifier_node
from nodes.retriever import retriever_node
from nodes.reasoner import reasoner_node

def route_by_intent(state):
    return state["intent"]

def build_query_graph():
    graph = StateGraph(GraphState)

    graph.add_node("classifier", classifier_node)
    graph.add_node("retriever", retriever_node)
    graph.add_node("reasoner", reasoner_node)

    graph.set_entry_point("classifier")

    graph.add_conditional_edges(
        "classifier",
        route_by_intent,
        {
            "lookup": "retriever",
            "reasoning": "retriever"
        }
    )

    graph.add_edge("retriever", "reasoner")
    graph.add_edge("reasoner", END)

    return graph.compile()
