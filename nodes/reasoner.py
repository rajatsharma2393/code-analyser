from llm.ollama_client import generate
from llm.prompts import build_prompt

def reasoner_node(state):
    chunks = state["retrieved_chunks"]

    if not chunks:
        return {
            **state,
            "answer": "No relevant code was found for this query."
        }

    prompt = build_prompt(state["query"], chunks)
    answer = generate(prompt)

    return {
        **state,
        "answer": answer
    }
