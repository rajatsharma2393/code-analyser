from langchain_ollama import ChatOllama

# initialize once
llm = ChatOllama(
    model="llama3.1",
    base_url="http://localhost:11434"
)

def generate(prompt: str) -> str:
    """Send prompt to Ollama and get response"""
    return llm.invoke(prompt)
