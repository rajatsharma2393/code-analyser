import numpy as np
from typing import List, Dict

class InMemoryVectorStore:
    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add(self, embedding: List[float], meta: Dict):
        self.vectors.append(np.array(embedding))
        self.metadata.append(meta)

    def all(self):
        return self.metadata

    def search(self, query_embedding, top_k=5):
        query = np.array(query_embedding)
        scores = []

        for idx, vec in enumerate(self.vectors):
            score = np.dot(query, vec) / (
                np.linalg.norm(query) * np.linalg.norm(vec)
            )
            scores.append((score, self.metadata[idx]))

        scores.sort(reverse=True, key=lambda x: x[0])
        return scores[:top_k]
