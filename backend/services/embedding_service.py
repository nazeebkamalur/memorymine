from sentence_transformers import SentenceTransformer

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text: str):
    if not text:
        text = "empty"

    embedding = model.encode(text, convert_to_numpy=True)
    return embedding.tolist()