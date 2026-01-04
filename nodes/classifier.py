def classifier_node(state):
    query = state["query"].lower()

    reasoning_keywords = [
        "what happens",
        "impact",
        "if i change",
        "flow",
        "why",
        "explain"
    ]

    intent = "lookup"
    for kw in reasoning_keywords:
        if kw in query:
            intent = "reasoning"
            break

    return {
        **state,
        "intent": intent
    }
