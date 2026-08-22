import faiss
import json
import os
import numpy as np

INDEX_PATH = "data/faiss.index"
META_PATH = "data/metadata/vector_metadata.json"

DIMENSION = 384

os.makedirs("data/metadata", exist_ok=True)

if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
else:
    index = faiss.IndexFlatL2(DIMENSION)

if os.path.exists(META_PATH):
    with open(META_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)
else:
    metadata = []


def save_index():
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)


def add_vector(embedding, memory):
    vector = np.array([embedding], dtype=np.float32)
    index.add(vector)
    metadata.append(memory)
    save_index()


# 🔥 IMPORTANT FIX
from services.embedding_service import create_embedding

def search_vectors(query):
    query_embedding = create_embedding(query)
    q = np.array([query_embedding], dtype=np.float32)

    distances, ids = index.search(q, 3)

    results = []
    for i in ids[0]:
        if i != -1 and i < len(metadata):
            results.append(metadata[i])

    return results