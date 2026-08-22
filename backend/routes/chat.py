from fastapi import APIRouter
from pydantic import BaseModel

from services.vector_service import search_vectors
from services.llm_service import generate_answer

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(req: ChatRequest):
    # CHANGE HERE 👇 (remove k=3)
    memories = search_vectors(req.question)

    if not memories:
        return {
            "answer": "No relevant memory found.",
            "results": []
        }

    answer = generate_answer(req.question, memories)

    return {
        "answer": answer,
        "results": memories
    }