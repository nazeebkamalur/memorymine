from fastapi import APIRouter
from pydantic import BaseModel

from services.embedding_service import create_embedding
from services.vector_service import search_vectors
from services.memory_service import get_all_memories

router = APIRouter()

class SearchRequest(BaseModel):
    query: str

@router.post("/")
async def semantic_search(request: SearchRequest):

    query_vector = create_embedding(request.query)

    nearest = search_vectors(query_vector, top_k=3)

    memories = get_all_memories()

    results = []

    for item in nearest:
        for memory in memories:
            if memory["id"] == item["memory_id"]:
                results.append({
                    "score": item["distance"],
                    "memory": memory
                })

    return results

