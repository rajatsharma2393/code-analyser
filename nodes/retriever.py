from embeddings import embed
from nodes.code_indexer import get_vector_store

store = get_vector_store()

def retriever_node(state):
    query_embedding = embed(state["query"])
    results = store.search(query_embedding, top_k=5)

    retrieved = [
        {
            "file": r[1]["file"],
            "type": r[1]["type"],
            "preview": r[1]["preview"],
            "score": float(r[0])
        }
        for r in results
    ]

    return {
        **state,
        "retrieved_chunks": retrieved
    }
