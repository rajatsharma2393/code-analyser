from typing import TypedDict, List, Literal, Dict

class GraphState(TypedDict):
    # input
    workspace_path: str
    query: str

    # classification
    intent: Literal["lookup", "reasoning"]

    # retrieval
    retrieved_chunks: List[Dict]

    # output
    answer: str
