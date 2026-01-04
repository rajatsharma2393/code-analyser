### Tests

Ollama:
brew install ollama
ollama serve



Ollama = a local LLM server + model manager

Runs as a background service on your machine

Downloads and serves models (LLaMA, Mistral, Phi, etc.)

Exposes an HTTP API (usually at http://localhost:11434)

Your Python / LangGraph / LangChain code just calls this API