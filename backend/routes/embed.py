from fastapi import APIRouter
from pydantic import BaseModel

from services.embedding_service import create_embedding

router = APIRouter()

class EmbedRequest(BaseModel):
    text: str

@router.post("/")
async def embed_text(request: EmbedRequest):
    embedding = create_embedding(request.text)

    return {
        "dimensions": len(embedding),
        "first_10_values": embedding[:10]
    }