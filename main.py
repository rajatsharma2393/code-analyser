from fastapi import FastAPI
from pydantic import BaseModel
from graph import build_graph
from nodes.code_indexer import get_vector_store

app = FastAPI()
graph = build_graph()
store = get_vector_store()

class IndexRequest(BaseModel):
    workspace_path: str

@app.post("/index")
def index_code(req: IndexRequest):
    return graph.invoke({
        "workspace_path": req.workspace_path
    })

@app.get("/debug/vectors")
def debug_vectors(limit: int = 5):
    data = store.all()[:limit]
    return {
        "stored_chunks": len(store.all()),
        "samples": data
    }
