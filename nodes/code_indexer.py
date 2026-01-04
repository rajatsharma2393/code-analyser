import os
from state import GraphState
from java_parser import extract_chunks
from embeddings import embed
from vector_store import InMemoryVectorStore

vector_store = InMemoryVectorStore()

def code_indexer_node(state: GraphState) -> GraphState:
    workspace = state["workspace_path"]
    indexed_chunks = 0

    for root, _, files in os.walk(workspace):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    code = f.read()

                chunks = extract_chunks(code)

                for chunk in chunks:
                    embedding = embed(chunk["code"])
                    vector_store.add(
                        embedding,
                        {
                            "file": path,
                            "type": chunk["type"],
                            "preview": chunk["code"][:200]
                        }
                    )
                    indexed_chunks += 1

    return {
        "workspace_path": workspace,
        "indexed_chunks": indexed_chunks
    }

def get_vector_store():
    return vector_store
