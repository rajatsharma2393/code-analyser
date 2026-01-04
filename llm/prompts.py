def build_prompt(query: str, chunks: list[dict]) -> str:
    context = "\n\n".join(
        f"File: {c['file']}\n{c['preview']}"
        for c in chunks
    )

    return f"""
You are a senior software assistant.

Answer the following question using ONLY the provided code context.

Question:
{query}

Code Context:
{context}

Explain clearly and concisely.
"""
