from fastapi import FastAPI
from pydantic import BaseModel

from graphs.index_graph import build_index_graph
from graphs.query_graph import build_query_graph

app = FastAPI()

index_graph = build_index_graph()
query_graph = build_query_graph()

class IndexRequest(BaseModel):
    workspace_path: str

class QueryRequest(BaseModel):
    query: str

@app.post("/index")
def index_codebase(req: IndexRequest):
    return index_graph.invoke({
        "workspace_path": req.workspace_path
    })

@app.post("/query")
def query_codebase(req: QueryRequest):
    return query_graph.invoke({
        "query": req.query
    })
