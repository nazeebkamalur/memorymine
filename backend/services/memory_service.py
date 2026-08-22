import os
import uuid
import tempfile
from fastapi import UploadFile

from services.ocr_service import extract_text
from services.embedding_service import create_embedding
from services.vector_service import add_vector

# RAM only (no JSON file, no uploads folder)
MEMORIES = []


# -----------------------------
# Save Memory (Privacy Mode)
# -----------------------------
async def save_memory(file: UploadFile):
    ext = os.path.splitext(file.filename)[1]

    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as temp:
        content = await file.read()
        temp.write(content)
        temp_path = temp.name

    try:
        # Extract text
        text = extract_text(temp_path)

        # Create embedding
        embedding = create_embedding(text)

        # Memory object (NO filepath stored)
        memory = {
            "id": str(uuid.uuid4()),
            "filename": file.filename,
            "text": text,
            "source_type": ext.replace(".", "")
        }

        # Store only in RAM
        MEMORIES.append(memory)

        # Add vector to FAISS
        add_vector(embedding, memory)

        return {
            "success": True,
            "memory": memory
        }

    finally:
        # Delete temp file immediately
        if os.path.exists(temp_path):
            os.remove(temp_path)


# -----------------------------
# Get All Memories
# -----------------------------
def get_all_memories():
    return list(reversed(MEMORIES))


# -----------------------------
# Delete Memory
# -----------------------------
def delete_memory(memory_id):
    global MEMORIES

    MEMORIES = [
        m for m in MEMORIES
        if m["id"] != memory_id
    ]

    return {"success": True}